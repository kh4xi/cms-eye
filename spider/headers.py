import requests

def check_headers(url):
    try:
        response = requests.get(url, timeout=10)
        headers = response.headers
        for key, value in headers.items():
            if "X-Generator" in key or "Powered-By" in key:
                return value
    except requests.exceptions.RequestException:
        return None
    return None