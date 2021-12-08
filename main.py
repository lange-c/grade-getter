from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
#from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
from webdriver_manager.utils import ChromeType

TIMEOUT = 20
USER_NAME = 'langec84'
USER_PW = 'Buster_123_'


def login(browser):
    browser.get("https://login.rowan.edu/cas/login?service=https%3A%2F%2Fbanner9.rowan.edu%3A443%2Fssomanager%2Fc%2FSSB")
    WebDriverWait(browser, TIMEOUT). \
        until(EC.visibility_of_element_located((By.ID, "username")))
    username = browser.find_element(By.ID, "username")
    username.send_keys(USER_NAME)
    password = browser.find_element(By.ID, "password")
    password.send_keys(USER_PW)
    browser.find_element(By.NAME, "submit").send_keys(Keys.RETURN)


def check_grades(browser):
    browser.get('https://banner9.rowan.edu/ords/ssb/bwskogrd.P_ViewGrde')
    headers = {'Accept': 'text/html',
               'Host': 'banner9.rowan.edu',
               'Origin': 'https://banner9.rowan.edu',
               'Cookie': 'SESSID=MEJEUFhHMTYzMjI4MzU=; _fbp=fb.1.1598565555762.1019820603; _hjid=4e2f32fe-6784-4cb9-b262-f1524e9bdd62; _gcl_au=1.1.95510286.1638392371; _hjSessionUser_82987=eyJpZCI6IjE4NDY2NDgwLTVlMzUtNWI4Zi1iNmQzLWQ2N2UwMGIzZDM5NiIsImNyZWF0ZWQiOjE2MzgzOTIzNzE0NjIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.794113766.1588195317; _ga_2H8XBMZ8Z5=GS1.1.1638480687.71.1.1638480720.27; NSC_MC-SPXBO-BTB-CBOOFS9-QSPE-PSET=ffffffff09f93eb545525d5f4f58455e445a4a421114; accessibility=false; NSC_JOv34o1hcoz10vjds2ljtodgkaelmeS=ffffffff09f93eb345525d5f4f58455e445a4a42112e; IDMSESSID=3EDB373727801DBE99F11C9C87836C102BFE0D731016C9CC708CEC296229EFF9D2E3576E2783FFEBFE483EF16DD7A70D'}
    payload = 'term_in=202140'
    response = browser.request('POST', 'https://banner9.rowan.edu/ords/ssb/bwskogrd.P_ViewGrde', headers=headers,
                               data=payload)
    sleep(3)
    print(f'{response} {response.headers} {response.content}')


def run():
    options = Options()
    # if use_user_data:
    #     options.add_argument('--user-data-dir=' + USER_DATA)
    options.add_argument('log-level=3')
    options.add_argument('--disable-extensions')
    options.add_argument("--disable-notifications")
    options.set_capability('unhandledPromptBehavior', 'dismiss')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # cdm = Service(ChromeDriverManager(log_level=0, print_first_line=False).install())
    browser = Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    # browser = Chrome(service=cdm, options=options)
    browser.set_window_size(1920, 1080)
    login(browser)
    check_grades(browser)
    browser.quit()


if __name__ == '__main__':
    run()
