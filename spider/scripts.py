import requests
from bs4 import BeautifulSoup

def check_scripts(url, cms_patterns):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        found_scripts = []

        for script in soup.find_all("script", src=True):
            script_src = script["src"]
            for pattern in cms_patterns.get("scripts", []):
                if pattern in script_src:
                    found_scripts.append(script_src)

        return found_scripts

    except requests.exceptions.RequestException:
        return []