import argparse
import os
from scan import Scan
from update import Update
from check import Check
import gevent.monkey
gevent.monkey.patch_all(ssl=False)

def main():
    parser = argparse.ArgumentParser(description="Usage:")
    sub_parsers = parser.add_subparsers(dest="module")
    
    scan_parsers = sub_parsers.add_parser("scan", help="scan Wordpress plugins and themes")
    scan_parsers.add_argument('-u', '--url', help='target url (e.g https://example.com)')
    scan_parsers.add_argument('-t', '--threads', help='number of threads to scan (default: 5)')
    scan_parsers.add_argument('-pl', '--plugin_list', help='specify plugins list to scan (default: all plugins -> please change the list until you feel hopeless)')
    scan_parsers.add_argument('-tl', '--theme_list', help='specify themes list to scan (default: all themes -> please change the list until you feel hopeless)')


    update_parsers = sub_parsers.add_parser("update", help="update Wordpress plugins and themes")

    check_parsers = sub_parsers.add_parser("check", help="check version of Wordpress plugins and themes")
    check_parsers.add_argument('-s', '--slug', help='specify Wordpress plugin or theme to check')
    check_parsers.add_argument('-v', '--version', help='specify Wordpress plugin or theme version to check vulnerabilities')

    args = parser.parse_args()
    if args.module == "scan":
        threads = 5
        plugins_list_path = os.getcwd() + "/list/all_plugins.txt"
        themes_list_path = os.getcwd() + "/list/all_themes.txt"
        if args.threads:
            threads = int(args.threads)
        if args.plugin_list:
            plugins_list_path = args.plugin_list
        if args.theme_list:
            themes_list_path = args.theme_list
        Scan.scan(args.url, threads, plugins_list_path, themes_list_path)
        return

    if args.module == "update":
        Update.update_plugins()
        return
    
    if args.module == "check":
        if args.slug and args.version:
            Check.check_version(args.slug, args.version)
        return

if __name__ == "__main__": 
    main()
