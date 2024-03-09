from bs4 import BeautifulSoup
import requests
import os

class Update:
    @staticmethod
    def update():
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0"
        }
        all_plugins = []
        over_1000_plugins = []
        over_2000_plugins = []
        over_5000_plugins = []
        over_10000_plugins = []
        over_20000_plugins = []
        page = 1
        while True:
            print(page)
            response = requests.get("https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[page]={}&request[per_page]=500".format(page), headers=headers).json()
            if not response["plugins"]:
                break
            for plugin in response["plugins"]:
                all_plugins.append(plugin["slug"])
                if plugin["active_installs"] >= 1000:
                    over_1000_plugins.append(plugin["slug"])
                if plugin["active_installs"] >= 2000:
                    over_2000_plugins.append(plugin["slug"])
                if plugin["active_installs"] >= 5000:
                    over_5000_plugins.append(plugin["slug"])
                if plugin["active_installs"] >= 10000:
                    over_10000_plugins.append(plugin["slug"])
                if plugin["active_installs"] >= 20000:
                    over_20000_plugins.append(plugin["slug"])
            page += 1
        with open(os.getcwd() + "/list/all_plugins.txt", "w") as file:
            file.write("\n".join(all_plugins))
        with open(os.getcwd() + "/list/over_1000_plugins.txt", "w") as file:
            file.write("\n".join(over_1000_plugins))
        with open(os.getcwd() + "/list/over_2000_plugins.txt", "w") as file:
            file.write("\n".join(over_2000_plugins))
        with open(os.getcwd() + "/list/over_5000_plugins.txt", "w") as file:
            file.write("\n".join(over_5000_plugins))
        with open(os.getcwd() + "/list/over_10000_plugins.txt", "w") as file:
            file.write("\n".join(over_10000_plugins))
        with open(os.getcwd() + "/list/over_20000_plugins.txt", "w") as file:
            file.write("\n".join(over_20000_plugins))
        print("Done!")