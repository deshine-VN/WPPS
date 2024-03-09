from urllib.parse import urlparse
import concurrent.futures
import re
import requests

class Scan:
    @staticmethod
    def is_url_alive(url):
        try:
            response = requests.head(url)
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
    def check_exist_plugin(url, plugin, filename):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"
        }
        response = requests.get("{}/wp-content/plugins/{}/{}".format(url, plugin, filename), headers=headers)
        if response.status_code == 200:
            print("Found plugin: {}".format(plugin))

    @staticmethod
    def scan(url, threads, list_path):
        if not Scan.is_valid_url(url) or not Scan.is_url_alive(url):
            print("Not a valid URL or URL is unreachable. Please check again!")
            return
        if url.endswith("/"):
            url = url[:-1]
        
        print("Scaning Plugins!")
        filenames = ["readme.txt", "README.txt", "README.md", "readme.md", "Readme.txt", "README.TXT", "ReadMe.txt", "changelog.txt", "changelog.md", "CHANGELOG.md"]
        plugins = None
        with open(list_path, "r") as file:
            content = file.read()
            plugins = content.split("\n")
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for plugin in plugins:
                for filename in filenames:
                    executor.submit(Scan.check_exist_plugin, url, plugin, filename)       