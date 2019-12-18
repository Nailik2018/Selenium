from Collections.MicrosoftLogin import MicrosoftLogin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

WEBDRIVER_PATH = r"D:\Entwicklung\Python\Selenium\chromedriver_win32\chromedriver.exe"
MICROSOFT_LOGIN_LINK = "https://login.live.com"
EMAIL_ADDRESS = "hansmustermann@hotmail.com"
EMAIL_PASSWORD = "122222"
EMAILFIELD = "i0116"
NEXTBUTTON = "idSIButton9"
PASSWORDFIELD = "i0118"

my_microsoft_login = MicrosoftLogin(EMAIL_ADDRESS, EMAIL_PASSWORD, WEBDRIVER_PATH, MICROSOFT_LOGIN_LINK)
my_microsoft_login.login(EMAILFIELD, PASSWORDFIELD, NEXTBUTTON)

exit()

browser = webdriver.Chrome(WEBDRIVER_PATH)
browser.get(MICROSOFT_LOGIN_LINK)

login = browser.find_element_by_id(EMAILFIELD)
login.clear()
time.sleep(1)
login.send_keys(EMAIL_ADDRESS)
time.sleep(1)
browser.find_element_by_id(NEXTBUTTON).click()

time.sleep(1)

pw = browser.find_element_by_id(PASSWORDFIELD)
pw.clear()
time.sleep(1)
pw.send_keys(EMAIL_PASSWORD)
time.sleep(1)
browser.find_element_by_id(NEXTBUTTON).click()



