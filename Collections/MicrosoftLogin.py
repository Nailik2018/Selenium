from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MicrosoftLogin():

    def __init__(self, username, pw, browser, microsoft_login_link):
        self.username = username
        self.pw = pw
        self.browser = browser
        self.microsoft_login_link = microsoft_login_link

    def login(self, email_field, pw_field, next_button):

        browser = webdriver.Chrome(self.browser)
        browser.get(self.microsoft_login_link)

        login = browser.find_element_by_id(email_field)
        login.clear()
        time.sleep(1)
        login.send_keys(self.username)
        time.sleep(1)
        browser.find_element_by_id(next_button).click()

        time.sleep(10)

        pw = browser.find_element_by_id(pw_field)
        pw.clear()
        time.sleep(1)
        pw.send_keys(self.pw)
        time.sleep(1)
        browser.find_element_by_id(next_button).click()

