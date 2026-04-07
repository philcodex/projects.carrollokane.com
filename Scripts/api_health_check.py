import requests
import time


# APIs to monitor
services = {
    "Stripe API": "https://api.stripe.com",
    "GitHub API": "https://api.github.com",
    "Status Page": "https://status.stripe.com"
}

# number of retries
MAX_RETRIES = 3

for service, url in services.items():

    print(f"\nChecking {service}")

    for attempt in range(1, MAX_RETRIES + 1):

        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                print(f"✓ {service} is healthy")
                break
            else:
                print(f"Attempt {attempt}: Unexpected status {response.status_code}")

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt}: Request failed: {e}")

        time.sleep(2)

    else:
        print(f"⚠ ALERT: {service} appears to be down after {MAX_RETRIES} attempts")