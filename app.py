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

    def toolbar(self):
        bot = self.bot
        # pobranie nazwy 1 zakladki
        quickbar_for_bot = bot.find_element_by_xpath(
            "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
        ).text
        if quickbar_for_bot != "Wioski":
            # przejscie do zakladek
            bot.find_element_by_xpath('//*[@id="ui_box"]/div[16]/div[1]/div[1]').click()
            time.sleep(1)
            count = 0
            while count != 6:
                # rozpoczecie usuwania wszystkich zkladek
                time.sleep(1)
                bot.find_element_by_xpath(
                    "/html/body/div[14]/div[2]/div[5]/div[2]/div/ul/li[1]/a"
                ).click()
                time.sleep(1)
                bot.find_element_by_xpath('//*[@id="remove_data"]').click()
                time.sleep(1)
                bot.find_element_by_xpath(
                    "/html/body/div[15]/div[2]/div[5]/div/div/a[1]"
                ).click()
                time.sleep(1)
                count += 1
            time.sleep(1)
            # dodanie zakladki dla bota
            bot.find_element_by_xpath('//*[@id="add_item_show"]').click()
            time.sleep(1)
            name = bot.find_element_by_xpath('//*[@id="toolbar_item_name"]')
            link = bot.find_element_by_xpath('//*[@id="toolbar_item_url"]')
            name.send_keys("Wioski")
            link.send_keys(
                'javascript:Layout.wnd.Create(Layout.wnd.TYPE_FARM_TOWN_OVERVIEWS,"Wioski rolnicze");void(0)'
            )
            bot.find_element_by_xpath('//*[@id="add_data"]').click()
            # zamkniecie zakladek
            time.sleep(1)
            bot.find_element_by_xpath("/html/body/div[14]/div[1]/a").click()

    def vialge_clicker(self):
        bot = self.bot
        while True:
            bot.find_element_by_xpath(
                "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
            ).click()
            timer = bot.find_element_by_xpath(
                '//*[@id="fto_claim_button"]'
            ).get_attribute("class")
            if not timer == "button button_new disabled active":
                bot.find_element_by_xpath(
                    '//*[@id="time_options_wrapper"]/div[1]/div[1]/a'
                ).click()
                bot.find_element_by_xpath('//*[@id="fto_claim_button"]/div[3]').click()
                time.sleep(60 * 5)

    def vilage_premium(self):
        bot = self.bot
        attempt = 0
        stop_c = 0
        cities_list = []
        selected_cities = []

        while attempt != 5:
            try:
                if villages == "1":
                    # pobieranie listy miast ktore moga otrzymywac surowce z wiosek
                    bot.find_element_by_xpath(
                        "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
                    ).click()
                    cities_query = bot.find_elements_by_class_name("fto_town")
                    # dodawanie mist do listy
                    for item in cities_query:
                        citie = item.find_element_by_class_name("gp_town_link").text
                        cities_list.append(citie)
                    if stop_c != 1:
                        print(
                            "Wybierz ktore miasta maja pobierac surowce, wpisujac liczby od 0-..."
                        )
                        print('Jesli nie chcesz podawac wiecej miast wpisz: "stop"')
                    # dodawanie wyboru miasta do listy
                    while stop_c != 1:
                        print(cities_list)
                        cities_choose = input()
                        if cities_choose == "stop":
                            stop_c = 1
                        else:
                            selected_cities.append(cities_choose)
                        sorted_cities_selected = list(set(selected_cities))

                        # TODO dopisac: wybieranie miast na podstawie wyboru, klikanie poboru surowcow i zatwierdzanie popapow

                elif villages == "2":
                    data.vialge_clicker()
                else:
                    break
            except:
                attempt += 1

    def exit(self):
        bot = self.bot
        bot.close()


# python app.py

data = GrepolisBot("login", "password")

print("Choose language: ")
language = input("1) Polish   2) English \n")
if language == "1":
    print("Czy masz wykupionego kapitana ?")
    option = input("1) Tak  2) Nie \n")
    print("Czy posiadasz wiecej miast z dostepem do wiosek niz 1 ?")
    villages = input("1) Tak  2) Nie \n")
    if option == "1":
        data.login_ac()
        data.toolbar()
        data.vilage_premium()
        data.exit()
    else:
        print("Coming soon")
elif language == "2":
    print("Do you have a redeemed captain?")
    option = input("1) Yes  2) No \n")
    if option == "1":
        data.login_ac()
        data.toolbar()
        data.vilage_premium()
        data.exit()
    else:
        print("Coming soon")
else:
    print("Wrong data! Write number")
