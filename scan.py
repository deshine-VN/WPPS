from urllib.parse import urlparse
from update import Update
from color import Color
from check import Check
import concurrent.futures
import re
import requests
import config
import truststore
import urllib3

urllib3.disable_warnings()
truststore.inject_into_ssl()

class Scan:
    @staticmethod
    def is_url_alive(url):
        try:
            response = requests.get(url, headers=config.headers)
            return response.status_code < 500
        except requests.exceptions.RequestException:
            return False
        
    @staticmethod
    def is_valid_url(url):
        try:
            result = urlparse(url)
            return result.scheme.lower().__eq__("http") or result.scheme.lower().__eq__("https")
        except ValueError:
            return False
        
    @staticmethod
    def detect_exist_plugin(url, plugin):
        url = "{}/plugins/{}/readme.txt".format(url, plugin)
        response = requests.get(url, headers=config.headers)
        if response.status_code == 200:
            version = re.findall(config.version_regex, response.text)
            version = version[0] if version else ""
            print("[{}] {} [{}]".format(Color.Green + plugin + Color.Reset, url, Color.Cyan + version + Color.Reset))
            Check.check_version(plugin, version)

    @staticmethod
    def detect_exist_theme(url, theme):
        url = "{}/themes/{}/readme.txt".format(url, theme)
        response = requests.get(url, headers=config.headers)
        if response.status_code == 200:
            version = re.findall(config.version_regex, response.text)
            version = version[0] if version else ""
            print("[{}] {} [{}]".format(Color.Green + theme + Color.Reset, url, Color.Cyan + version + Color.Reset))
            Check.check_version(theme, version)

    @staticmethod
    def scan(url, threads, plugins_list_path, themes_list_path):
        Update.update_vulnerabilities_database()
        if not Scan.is_valid_url(url) or not Scan.is_url_alive(url):
            print("[{}] URL seems invalid or unreachable. Please check again!".format(Color.Red + "ERROR" + Color.Reset))
            return
        print("[{}] The provided URL is valid and alive.".format(Color.Green + "OK" + Color.Reset))
        if url.endswith("/"):
            url = url[:-1]
        print("[{}] Scanning Plugins...It will take a while, please do not terminate this!\n...".format(Color.Yellow + "WARNING" + Color.Reset))
        plugins = None
        with open(plugins_list_path, "r") as file:
            content = file.read()
            plugins = content.split("\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for plugin in plugins:
                executor.submit(Scan.detect_exist_plugin, url, plugin)       
        
        themes = None
        with open(themes_list_path, "r") as file:
            content = file.read()
            themes = content.split("\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for theme in themes:
                executor.submit(Scan.detect_exist_theme, url, theme)       