from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class GrepolisBot:
    def __init__(self, login, password):
        self.bot = webdriver.Firefox()
        self.login = login
        self.password = password

    def login_ac(self):
        bot = self.bot
        bot.get("https://pl.grepolis.com/")
        time.sleep(2)
        login = bot.find_element_by_xpath('//*[@id="login_userid"]')
        password = bot.find_element_by_xpath('//*[@id="login_password"]')
        login.send_keys(self.login)
        password.send_keys(self.password)
        bot.find_element_by_xpath('//*[@id="login_Login"]').click()

    def vilage_premium(self):
        bot = self.bot


# python app.py

data = GrepolisBot("login", "password")
print("Choose language: ")
language = input("1) Polish   2) English \n")
if language == "1":
    print("Czy masz wykupionego kapitana ?")
    option = input("1) Tak  2) Nie \n")
    if option == "1":
        data.login_ac()
        # data.vilage_premium()
    else:
        print("Coming soon")
elif language == "2":
    print("Do you have a redeemed captain?")
    option = input("1) Yes  2) No \n")
    if option == "1":
        data.vilage_premium()
    else:
        print("Coming soon")
else:
    print("Wrong data! Write number")
