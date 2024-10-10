from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


import time
import random
from ua import useragent as ua
import zipfile

#################
#PROXY#
#################

PROXY_HOST = 'YOUR HOST' # rotating proxy or host
PROXY_PORT = 1234 # proxy port
PROXY_USER = 'USER' # username
PROXY_PASS = 'PASSWORD' # password

manifest_json = """
{
    "version": "1.0.0",
    "manifest_version": 2,
    "name": "Chrome Proxy",
    "permissions": [
        "proxy",
        "tabs",
        "unlimitedStorage",
        "storage",
        "<all_urls>",
        "webRequest",
        "webRequestBlocking"
    ],
    "background": {
        "scripts": ["background.js"]
    },
    "minimum_chrome_version":"22.0.0"
}
"""

background_js = """
var config = {
        mode: "fixed_servers",
        rules: {
        singleProxy: {
            scheme: "http",
            host: "%s",
            port: parseInt(%s)
        },
        bypassList: ["localhost"]
        }
    };

chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

function callbackFn(details) {
    return {
        authCredentials: {
            username: "%s",
            password: "%s"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
);
""" % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

plugin_file = 'proxy_auth_plugin.zip'

with zipfile.ZipFile(plugin_file, 'w') as zp:
    zp.writestr('manifest.json', manifest_json)
    zp.writestr('background.js', background_js)



options = webdriver.ChromeOptions()
options.add_extension(plugin_file)
options.add_argument(f"--user-agent={random.choice(ua)}")
options.add_argument("--window-size=1000,1800")
options.add_argument("--disable-notifications")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

username = ""
email = ""
password = ""
fullname = ""

try:
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    driver.implicitly_wait(10)

    email = driver.find_element(By.NAME, "emailOrPhone")

    name = driver.find_element(By.NAME, "fullName")

    u_name = driver.find_element(By.NAME, "username")
    
    paswd = driver.find_element(By.NAME, "password")
    time.sleep(1)

    email.send_keys(email)
    time.sleep(0.9)
    name.send_keys(fullname)
    time.sleep(1.3)
    u_name.send_keys(username)
    time.sleep(2.3)
    paswd.send_keys(password)
    time.sleep(3)
    paswd.send_keys(Keys.ENTER)
    time.sleep(5)                          


    month = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[4]/div/div/span/span[1]/select")
    day = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[4]/div/div/span/span[2]/select")
    year = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/div/div/div[1]/div/div/div[4]/div/div/span/span[3]/select")
    time.sleep(7)
    Select(month).select_by_value("1")
    time.sleep(1)
    Select(day).select_by_value("12")
    time.sleep(1.2)
    Select(year).select_by_value("1995")
    time.sleep(0.7)

    next_btn = driver.find_element(By.CSS_SELECTOR, "._acan._acap._acaq._acas._aj1-._ap30")
    time.sleep(0.9)
    action.move_to_element(next_btn).click().perform()
    time.sleep(1000)
except Exception as ex:
    print(ex)