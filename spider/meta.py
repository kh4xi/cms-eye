import requests
from bs4 import BeautifulSoup

def check_meta(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        meta_tag = soup.find("meta", attrs={"name": "generator"})
        if meta_tag and "content" in meta_tag.attrs:
            return meta_tag["content"],response.status_code
    except requests.exceptions.RequestException:
        return None
    return None