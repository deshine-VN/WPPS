import argparse
import os
from scan import Scan
from update import Update


def main():
    parser = argparse.ArgumentParser(description="Usage:")
    sub_parsers = parser.add_subparsers(help="Sub Modules", dest="module")
    
    scan_parsers = sub_parsers.add_parser("scan", help="Scan Wordpress Plugins")
    scan_parsers.add_argument('-u', '--url', help='Target URL (e.g https://example.com)')
    scan_parsers.add_argument('-t', '--threads', help='Number of threads to scan (Default is 5)')
    scan_parsers.add_argument('-l', '--list', help='Path of plugins list to scan (Default is all plugins -> Please change the list until you feel hopeless)')

    update_parsers = sub_parsers.add_parser("update", help="Update Wordpress Plugins")

    args = parser.parse_args()
    threads = 5
    list_path = os.getcwd() + "/list/all_plugins.txt"
    if args.module == "scan":
        if args.threads:
            threads = int(args.threads)
        if args.list:
            list_path = args.list
        Scan.scan(args.url, threads, list_path)
        return

    if args.module == "update":
        Update.update()
        return

if __name__ == "__main__": 
    main()