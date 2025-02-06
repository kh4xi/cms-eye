import json
import argparse
from spider.meta import check_meta
from spider.headers import check_headers
from spider.paths import check_paths

def load_patterns():
    with open("data/patterns.json", "r") as file:
        return json.load(file)

def detect_cms(url):
    cms_patterns = load_patterns()


    meta_info = check_meta(url)
    if meta_info:
        for cms, details in cms_patterns.items():
            if details["meta"].lower() in meta_info.lower():
                return f"CMS detected: {cms} (Meta Tag)"

    header_info = check_headers(url)
    if header_info:
        for cms, details in cms_patterns.items():
            if details["headers"].lower() in header_info.lower():
                return f"CMS detected: {cms} (Header)"


    for cms, details in cms_patterns.items():
        found_paths = check_paths(url, details)
        if found_paths:
            return f"CMS detected: {cms} (Paths: {', '.join(found_paths)})"

    return "CMS could not be detected"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CMS Finder Tool")
    parser.add_argument("url", help="Hedef URL")
    args = parser.parse_args()

    result = detect_cms(args.url)
    print(result)