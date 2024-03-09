import argparse
import os
from scan import Scan
from update import Update
from check import Check

def main():
    os.environ['OPENSSL_CONF'] = os.getcwd() + "/openssl.cnf"
    print(r"""
__        __            _ ____                                           
\ \      / /__  _ __ __| |  _ \ _ __ ___  ___ ___                        
 \ \ /\ / / _ \| '__/ _` | |_) | '__/ _ \/ __/ __|                       
  \ V  V / (_) | | | (_| |  __/| | |  __/\__ \__ \                       
 __\_/\_/ \___/|_|  \__,_|_|   |_| _\___||___/___/                       
|  _ \| |_   _  __ _(_)_ __  ___  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |_) | | | | |/ _` | | '_ \/ __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/| | |_| | (_| | | | | \__ \  ___) | (_| (_| | | | | | | |  __/ |   
|_|   |_|\__,_|\__, |_|_| |_|___/ |____/ \___\__,_|_| |_|_| |_|\___|_|   
               |___/                                                     
                        Author: deshine (https://hackerone.com/deshine)
""")
    
    parser = argparse.ArgumentParser(description="Usage:")
    sub_parsers = parser.add_subparsers(dest="module")
    
    scan_parsers = sub_parsers.add_parser("scan", help="Scan Wordpress Plugins")
    scan_parsers.add_argument('-u', '--url', help='target URL (e.g https://example.com)')
    scan_parsers.add_argument('-t', '--threads', help='number of threads to scan (default: 5)')
    scan_parsers.add_argument('-l', '--list', help='specify plugins list to scan (default: all plugins -> please change the list until you feel hopeless)')

    update_parsers = sub_parsers.add_parser("update", help="update Wordpress Plugins")

    check_parsers = sub_parsers.add_parser("check", help="check Version of Wordpress Plugins")
    check_parsers.add_argument('-p', '--plugin', help='specify Wordpress plugin to check')
    check_parsers.add_argument('-v', '--version', help='specify Wordpress plugin version to check')

    args = parser.parse_args()
    if args.module == "scan":
        threads = 5
        plugins_list_path = os.getcwd() + "/list/all_plugins.txt"
        if args.threads:
            threads = int(args.threads)
        if args.list:
            plugins_list_path = args.list
        Scan.scan(args.url, threads, plugins_list_path)
        return

    if args.module == "update":
        Update.update_plugins()
        return
    
    if args.module == "check":
        if args.plugin and args.version:
            Check.check_plugin_version(args.plugin, args.version)
        return

if __name__ == "__main__": 
    main()