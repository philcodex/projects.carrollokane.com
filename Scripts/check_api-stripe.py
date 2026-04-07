import requests

urls = [
    "https://api.github.com",
    "https://httpbin.org/status/500",
    "https://support.stripe.com",
    "https://httpbin.org/status/404"
]

def check(url):
    try:
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            return f"OK ({r.status_code})"
        if r.status_code == 404:
            return f" 404 Not Found: ({r.status_code})"
        else:
            return f"ERROR ({r.status_code})"

    except requests.exceptions.RequestException as e:
        return f"FAILED ({e})"


for url in urls:
    result = check(url)
    print(url, result)