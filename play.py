from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Collections.MicrosoftLogin import MicrosoftLogin

WEBDRIVER_PATH = r"D:\Entwicklung\Python\Selenium\chromedriver_win32\chromedriver.exe"
MICROSOFT_LOGIN_LINK = "https://login.live.com"
EMAIL_ADDRESS = "hansmustermann@hotmail.com"
EMAIL_PASSWORD = "123456"
EMAILFIELD = "i0116"
NEXTBUTTON = "idSIButton9"
PASSWORDFIELD = "i0118"


my_microsoft_login = MicrosoftLogin(EMAIL_ADDRESS, EMAIL_PASSWORD, WEBDRIVER_PATH, MICROSOFT_LOGIN_LINK)
my_microsoft_login.login(EMAILFIELD, PASSWORDFIELD, NEXTBUTTON)




