import argparse
from utils.banner import banner
from validate import stage_one, stage_two
import os

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')

print(banner())
parser = argparse.ArgumentParser(description="Stage selection based on command line argument")
parser.add_argument('--domain', '-d', help="Domain input for single search", type=str)
parser.add_argument('--full', '-f', help="Full subdomain search", type=str)

args = parser.parse_args()

if args.domain:
    stage_one(args.domain)

elif args.full:
    stage_two(args.full)
else:
    print("No valid argument provided. Please use --domain or --full.\n"
          "--domain or -d is for single domain pattern search\n"
          "--full or -f is for full subdomain pattern search")
