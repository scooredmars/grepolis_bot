from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

        # chose server
        time.sleep(3)
        bot.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[1]/div[2]/div[4]/form/div[2]/div/ul/li[1]"
        ).click()
        time.sleep(6)

    def vilage_premium(self):
        bot = self.bot
        bot.find_element_by_xpath('//*[@id="quickbar_dropdown0"]').click()
        while True:
            try:
                timer = bot.find_element_by_xpath(
                    '//*[@id="fto_claim_button"]'
                ).get_attribute("class")
                if not timer == "button button_new disabled active":
                    bot.find_element_by_xpath(
                        '//*[@id="time_options_wrapper"]/div[1]/div[1]/a'
                    ).click()
                    bot.find_element_by_xpath(
                        '//*[@id="fto_claim_button"]/div[3]'
                    ).click()
                    time.sleep(60 * 10)
                else:
                    data_unlock_time_str = bot.find_element_by_xpath(
                        '//*[@id="farm_town_list"]/div/ul/div/div/div[4]/div[3]'
                    ).text
                    # print(data_unlock_time_str[16:24])
            except:
                pass

    def exit(self):
        bot = self.bot
        bot.close()


# python app.py

data = GrepolisBot("login", "password")
data.login_ac()
data.vilage_premium()
data.exit()
"""
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
"""
