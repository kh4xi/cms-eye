import requests

def check_paths(url, cms_patterns):
    found_paths = []
    for path in cms_patterns.get("paths", []):
        full_url = url.rstrip("/") + path
        try:
            response = requests.get(full_url, timeout=5)
            if response.status_code == 200:
                found_paths.append(path)
        except requests.exceptions.RequestException:
            pass
    return found_paths