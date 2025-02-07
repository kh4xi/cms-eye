import requests

def check_protocol(url):
    if url is None or url.strip() == "":
        print("URL is None or empty, cannot check protocol")
        return None

    # Try HTTPS first
    https_url = f"https://{url}"
    try:
        response = requests.get(https_url, timeout=5)
        if response.status_code == 200:
            print("+ HTTPS is available")
            return https_url
    except requests.exceptions.RequestException as e:
        print(f" - HTTPS failed: {e}")

    # If HTTPS fails, try HTTP
    http_url = f"http://{url}"
    try:
        response = requests.get(http_url, timeout=5)
        if response.status_code == 200:
            print(" + Using HTTP instead of HTTPS")
            return http_url
    except requests.exceptions.RequestException as e:
        print(f" - HTTP failed: {e}")
        return None

    # If both HTTPS and HTTP fail, return None
    return None
