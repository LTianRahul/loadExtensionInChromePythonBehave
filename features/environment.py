from selenium import webdriver
import os
import json
from selenium.webdriver.chrome.options import Options
import subprocess


INDEX = int(os.environ['INDEX']) if 'INDEX' in os.environ else 0
if os.environ.get("env") == "jenkins":
    desired_cap_dict = os.environ["LT_BROWSERS"]
    CONFIG = json.loads(desired_cap_dict)
else:
    json_file = "config/config.json"
    with open(json_file) as data_file:
        CONFIG = json.load(data_file)

username = os.environ["LT_USERNAME"]
authkey = os.environ["LT_ACCESS_KEY"]

def before_feature(context, feature):
        chrome_extension = ["https://prod-magicleap-user-files-us-east-1-v1.s3.amazonaws.com/extensions/orgId-550422/3.56.0_0.zip"]

        options = Options()
        options.browser_version = "130"
        options.platform_name = "Windows 10"
        lt_options = {
            "username": "{LT_Username}",
            "accessKey": "{LT_AccessKey}",
            "project": "Untitled",
            "lambda:loadExtension": chrome_extension,
            "browserName": "Chrome",
            "name": "Load Extension Testing",
            "build": "Chrome Extension in Python-Behave"
        }
        options.set_capability('LT:Options', lt_options)
        
        context.driver = webdriver.Remote(
            command_executor="http://{LT_Username}:{LT_AccessKey}@hub.lambdatest.com/wd/hub".format(
                lt_options["username"], lt_options["accessKey"]),
            options=options)
 
def after_feature(context, feature):
    context.driver.quit()
