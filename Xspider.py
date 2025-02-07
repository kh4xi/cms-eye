import json
from spider.meta import check_meta
from spider.headers import check_headers
from spider.paths import check_paths
from utils.colors import MyColors
# from spider.subdomain import main
confidence = 0

def load_patterns():
    with open("data/patterns.json", "r") as file:
        return json.load(file)

class Spider:
    def __init__(self, url):
        if not url:
            raise ValueError("URL cannot be None or empty")
        self.url = url
        self.patterns = load_patterns()
        self.meta_info = check_meta(self.url)
        self.header_info = check_headers(self.url)
        self.paths = check_paths(url, self.patterns)

    def search_for_meta(self, cms_patterns=None):
        global confidence
        if cms_patterns is None:
            cms_patterns = load_patterns()

        if not self.url:
            print(f"{MyColors.colorize_text(' - URL is None!', MyColors.r_color)}")
            return False

        meta_info = check_meta(self.url)
        if meta_info:
            for cms, details in cms_patterns.items():
                if details["meta"].lower() in meta_info.lower():
                    print(
                        f" {MyColors.colorize_text(' + CMS detected', MyColors.g_color)}: {cms} Meta Tag: {details['meta'].lower()}")
                    confidence += 1
                    return True
        else:
            print(f" {MyColors.colorize_text(' - No Meta tag detected !', MyColors.r_color)}")
            return False

    def search_for_headers(self, cms_patterns=None):
        global confidence
        if cms_patterns is None:
            cms_patterns = load_patterns()

        if not self.url:
            print(f"{MyColors.colorize_text(' - URL is None!', MyColors.r_color)}")
            return False

        header_info = check_headers(self.url)
        if header_info:
            for cms, details in cms_patterns.items():
                if details["headers"].lower() in header_info.lower():
                    print(
                        f" {MyColors.colorize_text(' + CMS detected', MyColors.g_color)}: {cms} \n Header value: {details['headers'].lower()}")
                    confidence += 1
                    return True
        else:
            print(f" {MyColors.colorize_text(' - No Header detected !', MyColors.r_color)}")
            return False

    def search_for_paths(self, cms_patterns=None):
        global confidence
        if cms_patterns is None:
            cms_patterns = load_patterns()

        if not self.url:
            print(f"{MyColors.colorize_text(' - URL is None!', MyColors.r_color)}")
            return False

        detected = []
        for cms, details in cms_patterns.items():
            # print(f"Checking paths for CMS: {cms}, Details: {details}") # Debug
            found_paths = check_paths(self.url, details)
            # print(f"Found paths: {found_paths}")   # Debug

            if found_paths:
                detected.append(f"{cms} (Paths: {', '.join(found_paths)})")
                confidence += 1

        if detected:
            print(f" {MyColors.colorize_text(' + Path detected', MyColors.g_color)} " + "\n + ".join(detected))
        else:
            print(f"{MyColors.colorize_text(' - No path detected !', MyColors.r_color)}")
"""
def test_spider(url):
    try:
        spider = Spider(url)

        print(f"Testing Meta Search: {spider.url}")
        if spider.search_for_meta():
            print("Meta search successful.")
        else:
            print("Meta search failed.")

        print("\nTesting Header Search:")
        if spider.search_for_headers():
            print("Header search successful.")
        else:
            print("Header search failed.")

        print("\nTesting Path Search:")
        if spider.search_for_paths():
            print("Path search successful.")
        else:
            print("Path search failed.")

    except ValueError as e:
        print(f"Error: {e}")

bitest = main('website.tld')
counter = 0
print("\n\n")
for subdomain in bitest:
    print(f"{subdomain}\n")
    test_spider(subdomain)
    counter += 1

print(f"counter {counter}")
print(f"total length{bitest}")
print(len(bitest))"""