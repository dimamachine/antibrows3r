import re
import zipfile
import random
import msvcrt
from sys import __stdout__
from multiprocessing import Pool

from loguru import logger
from decouple import config
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ua = UserAgent(browsers=["chrome"])

list_chrome = [
    "Chrome/70.0.3538.77",
    "Chrome/99.0.4844.84",
    "Chrome/103.0.5060.53",
    "Chrome/104.0.0.0",
    "Chrome/104.0.5112.79",
]

PROXY_HOST = config("PROXY_HOST", default="")
PROXY_PORT = int(config("PROXY_PORT"))  # Your proxy port
PROXY_USER = config("PROXY_USER", default="")
PROXY_PASS = config("PROXY_PASS", default="")

logger.info(f"{PROXY_HOST} {PROXY_PORT} {PROXY_USER} {PROXY_PASS}")

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
    "minimum_chrome_version":"76.0.0"
}
"""

background_js = """
let config = {
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
""" % (
    PROXY_HOST,
    PROXY_PORT,
    PROXY_USER,
    PROXY_PASS,
)


def _set_chrome(user_agent: str) -> str:
    set_ch = re.compile(r"Chrome\/[\S]*")
    user_agent = set_ch.sub(
        list_chrome[random.randint(0, len(list_chrome) - 1)], user_agent
    )
    return user_agent


def get_chromedriver(windows=None, use_proxy=False, user_agent=None):
    chrome_options = webdriver.ChromeOptions()

    if use_proxy:
        plugin_file = "proxy_auth_plugin.zip"
        logger.info(f"Proxy {use_proxy}")

        with zipfile.ZipFile(plugin_file, "w") as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        chrome_options.add_extension(plugin_file)

    user_agent = _set_chrome(user_agent)
    if user_agent:
        chrome_options.add_argument(f"--user-agent={user_agent}")
        logger.info(f"User-agent {user_agent}")

    s = Service(executable_path="path_to_chromedriver")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.set_window_size(600, 1000)

    driver.set_window_position(windows[0], windows[1])

    return driver


def main(windows: int) -> None:
    driver = get_chromedriver(
        windows=windows,
        use_proxy=True,
        user_agent=ua.random,
    )
    driver.get("https://twitter.com")
    while True: 
        if msvcrt.kbhit(): #если нажата клавища
            k = ord(msvcrt.getch()) #считываем код клавиши
            if k == 27: # если клавиша Esc
                driver.close()
                driver.quit()
                driver.ejjg()



if __name__ == "__main__":
    with Pool(processes=10) as p:
        windows = [[600 * i % 1800, 0] for i in range(10)]
        p.map(main, windows)
