import Xspider
from utils.verify_protocol import check_protocol
from spider.subdomain import main
from urllib.parse import urlparse, urljoin

def stage_one(url):
    print(f"Original URL: {url}")
    if not url:
        raise ValueError("URL is empty or None")
    if 'www.' in url:
        url = url.replace('www.', '', 1)
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    parsed_url = urlparse(url)
    hostname = parsed_url.netloc
    full_url = check_protocol(hostname)
    print(f"Parsed URL with protocol: {full_url}")

    if not full_url:
        print(f" - Invalid URL after protocol check for {url}. Skipping...")
        return

    spider = Xspider.Spider(url=full_url)
    print(f"\n\n + Checking for: {spider.url}\n")

    if spider.search_for_meta() is True:
        return
    if spider.search_for_headers() is True:
        return
    spider.search_for_paths()

def stage_two(url):
    subdomains = main(url)
    processed_subdomains = set()
    print(f"\n\n + Checking for subdomains of: {url}\n\n")

    for dom in subdomains:
        if dom in processed_subdomains:
            print(f" - Subdomain {dom} has already been tested. Skipping...")
            continue

        # Ensure subdomains have a protocol
        if not dom.startswith(('http://', 'https://')):
            dom = 'http://' + dom


        if 'www.' in dom:
            dom = dom.replace('www.', '', 1)

        parsed_url = urlparse(dom)
        domain_part = parsed_url.netloc.split('/')[0]


        if domain_part.count(domain_part.split('.')[0]) > 1:
            print(f" - Invalid subdomain detected (double domain part): {dom}. Skipping...")
            continue


        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"


        if parsed_url.path:
            full_url = urljoin(base_url, parsed_url.path)
        else:
            full_url = base_url

        if '..' in full_url:
            print(f" - Skipping invalid URL with double dots: {full_url}")
            continue

        print(f"Parsed Subdomain: {full_url}")
        stage_one(full_url)

        processed_subdomains.add(dom)


# stage_two('test.tld')
# stage_one('test.tld')