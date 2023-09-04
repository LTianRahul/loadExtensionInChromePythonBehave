from selenium import webdriver
import os
import json
from selenium.webdriver.firefox.options import Options
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
        options =  Options()
        options.browser_version = "114.0"
        options.platform_name = "Windows 10"
        lt_options = {};
        lt_options["username"] = "";
        lt_options["accessKey"] = "";
        lt_options["browserName"] = "Chrome";
        lt_options["browserVersion"] = "latest";
        # lt_options["tunnel"] = True;
        lt_options["build"] = "TestingSampleBehavePython";
        lt_options["w3c"] = True;
        lt_options["plugin"] = "python-python";
        lt_options["selenium_version"] = "4.10.0";
        options.set_capability('LT:Options', lt_options);
        # "browserName": "Chrome",
		# "browserVersion": "latest"
        # Steps to run Smart UI project (https://beta-smartui.lambdatest.com/)
        # Step - 1 : Change the hub URL to @beta-smartui-hub.lambdatest.com/wd/hub
        # Step - 2 : Add "smartUI.project": "<Project Name>" as a capability above
        # Step - 3 : Run "driver.execute_script("smartui.takeScreenshot")" command wherever you need to take a screenshot
        # Note: for additional capabilities navigate to https://www.lambdatest.com/support/docs/test-settings-options/
        context.driver = webdriver.Remote(
            command_executor="http://rahulkumarlambdatest:dboZK7so8koMnIR1tN11aKfMgxyKtDpb90IlyaCj4n6n7tQeK6@hub.lambdatest.com/wd/hub".format(
                lt_options["username"], lt_options["accessKey"]),
            options=options)
 

# def before_feature(context, feature):
#     desired_cap = setup_desired_cap(CONFIG[INDEX])
#     context.browser = webdriver.Remote(
#         desired_capabilities=desired_cap,
#         command_executor="https://%s:%s@hub.lambdatest.com:443/wd/hub" % (username, authkey)
#     )


def after_feature(context, feature):
    context.driver.quit()

# if __name__ == "__main__":

# 	#start tunnel process
# 	tunnel_process = subprocess.Popen(["./LT","--user",username,"--key",authkey],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
	
# 	# #run testcases
# 	# unittest.main()

# 	#end tunnel
# 	tunnel_process.terminate()


     
# def setup_desired_cap(desired_cap):
#     """
#     sets the capability according to LT
#     :param desired_cap:
#     :return:
#     """
#     return desired_cap
