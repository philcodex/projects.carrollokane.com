import time
import requests
from app import app
from models import db, HealthCheck

SERVICES = {
    "GitHub API": "https://api.github.com",
    "Stripe Status": "https://status.stripe.com",
    "Python Docs": "https://docs.python.org/3/"
}

MAX_RETRIES = 3
TIMEOUT = 5


def check_service(service_name, url):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=TIMEOUT)
            end_time = time.time()

            response_time_ms = round((end_time - start_time) * 1000, 2)

            if response.status_code == 200:
                return {
                    "status_code": response.status_code,
                    "is_up": True,
                    "response_time_ms": response_time_ms,
                    "error_message": None,
                }

        except requests.exceptions.RequestException as exc:
            error_message = str(exc)

        time.sleep(2)

    return {
        "status_code": None,
        "is_up": False,
        "response_time_ms": None,
        "error_message": error_message if "error_message" in locals() else "Unknown error",
    }


def run_checks():
    with app.app_context():
        for service_name, url in SERVICES.items():

            result = check_service(service_name, url)

            # ALERT if service is down
            if not result["is_up"]:
                print(f"ALERT: {service_name} is down")

            check = HealthCheck(
                service_name=service_name,
                url=url,
                status_code=result["status_code"],
                is_up=result["is_up"],
                response_time_ms=result["response_time_ms"],
                error_message=result["error_message"],
            )

            db.session.add(check)

        db.session.commit()


if __name__ == "__main__":
    run_checks()

    if not result["is_up"]:
    print(f"ALERT: {service_name} is down")
