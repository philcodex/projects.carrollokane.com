"""Monitor key API endpoints with retries and logging."""

import logging
import time
import requests

# Configuration
SERVICES = {
    "GitHub API": "https://api.github.com",
    "Stripe Status Page": "https://status.stripe.com",
}

MAX_RETRIES = 3
REQUEST_TIMEOUT = 5
RETRY_DELAY_SECONDS = 2

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)


def check_service(service_name: str, url: str) -> bool:
    """Check a service endpoint and retry on failure.

    Returns True if the service responds with HTTP 200 within the retry limit.
    Returns False if all retry attempts fail.
    """
    logging.info("Checking %s at %s", service_name, url)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)

            if response.status_code == 200:
                logging.info(
                    "%s is healthy (status code %s)",
                    service_name,
                    response.status_code,
                )
                return True

            logging.warning(
                "Attempt %s/%s for %s returned unexpected status code %s",
                attempt,
                MAX_RETRIES,
                service_name,
                response.status_code,
            )

        except requests.exceptions.RequestException as exc:
            logging.error(
                "Attempt %s/%s for %s failed: %s",
                attempt,
                MAX_RETRIES,
                service_name,
                exc,
            )

        time.sleep(RETRY_DELAY_SECONDS)

    else:
        logging.critical(
            "ALERT: %s appears to be unavailable after %s attempts",
            service_name,
            MAX_RETRIES,
        )
        return False


def main() -> None:
    """Run health checks for all configured services."""
    results = {}

    for service_name, url in SERVICES.items():
        results[service_name] = check_service(service_name, url)

    logging.info("Health check summary: %s", results)


if __name__ == "__main__":
    main()