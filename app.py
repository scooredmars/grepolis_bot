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
        server_list = {}
        server_name_list = {}
        server_key = 0
        choosing_server = True
        server_choosed_list = []
        bot.get("https://pl.grepolis.com/")
        time.sleep(2)
        login = bot.find_element_by_xpath('//*[@id="login_userid"]')
        password = bot.find_element_by_xpath('//*[@id="login_password"]')
        login.send_keys(self.login)
        password.send_keys(self.password)
        bot.find_element_by_xpath('//*[@id="login_Login"]').click()

        # wybor servera
        time.sleep(3)
        world_name = bot.find_elements_by_class_name("world_name")
        for a in world_name:
            b = a.get_attribute("data-worldname")
            server_key += 1
            server_name_list[server_key] = b
            server_list[server_key] = a
        print(
            "Wybierz numer servera z listy: \n",
            server_name_list,
        )
        print('Jesli nie chcesz podac wiecej miast wpisz: "0"')
        while choosing_server == True:
            server_choosed = int(input())
            if server_choosed != 0:
                server_choosed_list.append(server_choosed)
            elif server_choosed == 0:
                choosing_server = False
            else:
                print("zla wartosc!!")
        for a in server_choosed_list:
            server_list[a].click()
            time.sleep(1)
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

    def village_clicker(self):
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
                time.sleep(time_sleep)

    def village(self):
        bot = self.bot
        attempt = 0
        cities_list = {}
        town_checkbox_list = {}
        cities_choosed_list = []
        key_citie = 0
        key_checkbox = 0
        lock_loop = False
        continue_choosing = True

        while attempt != 5:
            try:
                if villages == "1":
                    if one_citie_in_one_island == "1":
                        if lock_loop == False:
                            # pobieranie listy miast ktore moga otrzymywac surowce z wiosek
                            bot.find_element_by_xpath(
                                "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
                            ).click()
                            cities_query = bot.find_elements_by_class_name("fto_town")
                            town_checkbox = bot.find_elements_by_class_name("town_checkbox")
                            # dodawanie miast do listy
                            for item in cities_query:
                                citie = item.find_element_by_class_name(
                                    "gp_town_link"
                                ).text
                                key_citie += 1
                                cities_list[key_citie] = citie
                            # dodawanie checkbox'ow miast do listy
                            for checkbox in town_checkbox:
                                key_checkbox += 1
                                town_checkbox_list[key_checkbox] = checkbox
                            print(
                                "Wybierz numer miasta do zbiorow z listy (pamietaj tylko 1 miasto na wyspe!!!): \n",
                                cities_list,
                            )
                            print('Jesli nie chcesz podac wiecej miast wpisz: "0"')
                            while continue_choosing == True:
                                cities_choosed = int(input())
                                if cities_choosed != 0:
                                    cities_choosed_list.append(cities_choosed)
                                elif cities_choosed == 0:
                                    continue_choosing = False
                                else:
                                    print("zla wartosc!!")
                                cities_choosed_list = list(set(cities_choosed_list))
                            lock_loop = True
                        # pobranie listy wybranych miast uzytkownika i zaznaczenie je w panelu
                        for key in cities_choosed_list:
                            town_checkbox_list[key].click()
                            time.sleep(1)
                        # odbierz
                        bot.find_element_by_xpath('//*[@id="fto_claim_button"]').click()
                        time.sleep(1)
                        # potweirdzenie
                        bot.find_element_by_xpath(
                            "/html/body/div[15]/div/div[11]/div/div[2]/div[1]"
                        ).click()
                        time.sleep(time_sleep)

                    elif one_citie_in_one_island == "2":
                        bot.find_element_by_xpath(
                            "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
                        ).click()
                        time.sleep(2)
                        # checkbox
                        bot.find_element_by_xpath(
                            "/html/body/div[14]/div[2]/div[5]/div[1]/div/div[9]/span/a"
                        ).click()
                        time.sleep(1)
                        bot.find_element_by_xpath('//*[@id="fto_claim_button"]').click()
                        time.sleep(1)
                        # potweirdzenie
                        bot.find_element_by_xpath(
                            "/html/body/div[15]/div/div[11]/div/div[2]/div[1]"
                        ).click()
                    time.sleep(time_sleep)
                    # TODO dopisac: wybieranie miast na podstawie wyboru usera, klikanie poboru surowcow i zatwierdzanie

                elif villages == "2":
                    data.village_clicker()
                else:
                    break
            except:
                attempt += 1
                print("Error nr.", attempt)

    def exit(self):
        bot = self.bot
        bot.close()


# pipenv shell
# python app.py

data = GrepolisBot("login", "haslo")
villages = input(
    "Czy posiadasz wiecej miast z dostepem do wiosek niz 1 ? \n 1) Tak  2) Nie \n"
)
buff = input('Czy masz odblokowana "Lojalnosc Chlopow" ? \n 1) Tak  2) Nie \n')
if villages == "1":
    one_citie_in_one_island = input(
        "Czy posiadasz 2 lub wiecej miast na tej samej wyspie? \n 1) Tak  2) Nie \n"
    )
if buff == "1":
    time_sleep = 60 * 10
elif buff == "2":
    time_sleep = 60 * 5

data.login_ac()
data.toolbar()
data.village()
data.exit()
