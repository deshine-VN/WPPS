from color import Color
import config
import hashlib
import requests
import json
import os

class Update:
    @staticmethod
    def update_plugins():
        print("[{}] {}".format(Color.Yellow + "WARNING" + Color.Reset, "Updating plugins!!!"))
        all = []
        page = 1
        while True:
            print(page)
            response = requests.get("https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[page]={}&request[per_page]=500".format(page), headers=config.headers).json()
            if not response["plugins"]:
                break
            for plugin in response["plugins"]:
                all.append(plugin["slug"])
            page += 1

        print("[{}] {}".format(Color.Yellow + "WARNING" + Color.Reset, "Updating themes!!!"))
        page = 1
        while True:
            print(page)
            response = requests.get("https://api.wordpress.org/themes/info/1.2/?action=query_themes&request[page]={}&request[per_page]=500".format(page), headers=config.headers).json()
            if not response["themes"]:
                break
            for theme in response["themes"]:
                all.append(theme["slug"])
            page += 1
        with open(os.getcwd() + "/list/all.txt", "w") as file:
            file.write("\n".join(all))
        print("[{}] {}".format(Color.Green + "OK" + Color.Reset, "Update successfully."))

    @staticmethod
    def is_new_vulnerabilities_database():
        response = requests.get("https://www.wordfence.com/api/intelligence/v2/vulnerabilities/production")
        new_hash = hashlib.md5(response.content).hexdigest()
        with open(os.getcwd() + "/database/wordfence.json", "rb") as file:
            content = file.read()
            current_hash = hashlib.md5(content).hexdigest()
            if current_hash == new_hash:
                return False
        with open(os.getcwd() + "/database/wordfence.json", "wb") as file:
            file.write(response.content)
            return True

    @staticmethod
    def update_vulnerabilities_database():
        if Update.is_new_vulnerabilities_database():
            print("[{}] {}".format(Color.Yellow + "WARNING" + Color.Reset, "There is a new version of vulnerabilities database. Updating ..."))
            database = {}
            with open(os.getcwd() + "/database/wordfence.json", "r") as file:
                content = file.read()
                vulnerabilities = json.loads(content)
                for vulnerability in vulnerabilities:
                    try:
                        database[vulnerabilities[vulnerability]["software"][0]["slug"]].append({
                            "title": vulnerabilities[vulnerability]["title"],
                            "cve": vulnerabilities[vulnerability]["cve"],
                            "affected_versions": vulnerabilities[vulnerability]["software"][0]["affected_versions"]
                        })
                    except:
                        database[vulnerabilities[vulnerability]["software"][0]["slug"]] = []
                        database[vulnerabilities[vulnerability]["software"][0]["slug"]].append({
                            "title": vulnerabilities[vulnerability]["title"],
                            "cve": vulnerabilities[vulnerability]["cve"],
                            "affected_versions": vulnerabilities[vulnerability]["software"][0]["affected_versions"]
                        })
            
            with open(os.getcwd() + "/database/database.json", "w") as file:
                file.write(json.dumps(database))
            print("[{}] {}".format(Color.Green + "OK" + Color.Reset, "Update successfully."))