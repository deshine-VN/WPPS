from packaging import version
from color import Color
import json
import os

class Check:
    @staticmethod
    def compare_version(current_version, from_version, to_version):
        if from_version == "*":
            from_version = "0"
        if version.parse(from_version) <= version.parse(current_version) <= version.parse(to_version):
            return True
        else:
            return False

    @staticmethod
    def check_version(plugin, version):
        with open(os.getcwd() + "/database/database.json", "r") as file:
            content = file.read()
            database = json.loads(content)
            vulnerabilities = database[plugin]
            for vulnerability in vulnerabilities:
                affected_versions = vulnerability["affected_versions"]
                for affected_version in affected_versions:
                    if Check.compare_version(version, affected_versions[affected_version]["from_version"], affected_versions[affected_version]["to_version"]):
                        print("==> [{}] [{}] [{}] [{}] ".format(Color.Red + "VULNERABLE" + Color.Reset, 
                                                               Color.Green + plugin + Color.Reset, 
                                                               Color.Yellow + vulnerability["title"] + Color.Reset,
                                                               Color.Red + str(vulnerability["cve"]) + Color.Reset))