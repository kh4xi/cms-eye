import sys

import requests
from utils.colors import MyColors


wildcards_list = set()
domain_list = set()


def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            subdomains = set()
            data = response.json()
            for entry in data:
                subdomains.add(entry['name_value'])
            return subdomains
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def check_wildcards(domain):
    subdomains = get_subdomains(domain)
    if subdomains:
        for subdomain in subdomains:
            if '*' in subdomain:
                wildcards_list.add(subdomain)
            else:
                domain_list.add(subdomain)
    else:
        print(f"{MyColors.colorize_text(" - No subddomains found", MyColors.r_color)}:{domain}")


def main(arg):
    check_wildcards(arg)
    if not wildcards_list and not domain_list:
        print(f"{MyColors.colorize_text(' - No subdomains found', MyColors.r_color)}:{arg}")
    else:
        print(f"{MyColors.colorize_text('Passing wildcard values : (note that these are ignored!)', MyColors.y_color)} \n")
        for subdomain in wildcards_list:
            print(subdomain)

        print(f"\n\n {MyColors.colorize_text('Analyzing these domains', MyColors.w_color)}:\n\n ")
        for domain in domain_list:
            print(domain)

    return domain_list
"""
if __name__ == '__main__':
    bitest = main('test.tld')
    for subdomain in bitest:
        print(subdomain)

"""