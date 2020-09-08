from selenium import webdriver
import time


class GrepolisBot:
    def __init__(self, login, password):
        self.bot = webdriver.Firefox()
        self.login = login
        self.password = password

    def account_login(self):
        bot = self.bot
        bot.get("https://pl.grepolis.com/")
        time.sleep(2)
        login = bot.find_element_by_xpath('//*[@id="login_userid"]')
        password = bot.find_element_by_xpath('//*[@id="login_password"]')
        login.send_keys(self.login)
        password.send_keys(self.password)
        bot.find_element_by_xpath('//*[@id="login_Login"]').click()

    def server_choose(self):
        bot = self.bot
        world_name_list = {}
        world_xpath_list = {}
        world_counter = []
        server_key = 0

        time.sleep(2)
        world_names_qs = bot.find_elements_by_class_name("world_name")
        for world in world_names_qs:
            name = world.get_attribute("data-worldname")
            server_key += 1
            world_name_list[server_key] = name
            world_xpath_list[server_key] = world
            world_counter.append(name)
        time.sleep(1)
        if len(world_counter) == 1:
            world_xpath_list[1].click()
        else:
            print(world_name_list,"\nWybierz server podajac numer z przed jego nazwy:")
            world_choosed = int(input())
            world_xpath_list[world_choosed].click()
        time.sleep(6)

    def toolbar(self):
        bot = self.bot
        toolbar_count = 0

        # get name of 1 tab
        quickbar_for_bot = bot.find_element_by_xpath(
            "/html/body/div[1]/div[16]/div[1]/div[2]/div/div"
        ).text
        if quickbar_for_bot != "Wioski":
            # go to tabs
            bot.find_element_by_xpath('//*[@id="ui_box"]/div[16]/div[1]/div[1]').click()
            time.sleep(1)
            while toolbar_count != 6:
                # start removing all tabs
                time.sleep(1)
                bot.find_element_by_class_name("id_"+str(toolbar_count)).click()
                time.sleep(1)
                bot.find_element_by_xpath('//*[@id="remove_data"]').click()
                time.sleep(1)
                # confirm button
                bot.find_element_by_xpath(
                    "/html/body/div[15]/div[2]/div[5]/div/div/a[1]"
                ).click()
                time.sleep(1)
                toolbar_count += 1
            time.sleep(1)
            # add tab for bot
            bot.find_element_by_xpath('//*[@id="add_item_show"]').click()
            time.sleep(1)
            name = bot.find_element_by_xpath('//*[@id="toolbar_item_name"]')
            link = bot.find_element_by_xpath('//*[@id="toolbar_item_url"]')
            name.send_keys("Wioski")
            link.send_keys(
                'javascript:Layout.wnd.Create(Layout.wnd.TYPE_FARM_TOWN_OVERVIEWS,"Wioski rolnicze");void(0)'
            )
            bot.find_element_by_xpath('//*[@id="add_data"]').click()
            # close tabs
            time.sleep(1)
            bot.find_element_by_class_name("ui-dialog-titlebar-close").click()

    def one_city(self):
        bot = self.bot
        while True:
            bot.find_element_by_id("quickbar_dropdown0").click()
            timer = bot.find_element_by_xpath(
                '//*[@id="fto_claim_button"]'
            ).get_attribute("class")
            if timer != "button button_new disabled active":
                # set time
                bot.find_element_by_xpath(
                    '//*[@id="time_options_wrapper"]/div[1]/div[1]/a'
                ).click()
                bot.find_element_by_xpath('//*[@id="fto_claim_button"]').click()
                time.sleep(time_sleep)

    def more_cities_different_island(self):
        bot = self.bot
        bot.find_element_by_id("quickbar_dropdown0").click()
        time.sleep(2)
        bot.find_element_by_class_name("select_all").click()
        time.sleep(1)
        bot.find_element_by_xpath('//*[@id="fto_claim_button"]').click()
        time.sleep(1)
        bot.find_element_by_class_name("btn_confirm").click()
        time.sleep(time_sleep)

    def village_clicker(self):
        bot = self.bot
        lock_loop = False
        continue_choosing = True
        key_citie = 0
        key_checkbox = 0
        attempt = 0
        cities_list = {}
        cities_checkbox_list = {}
        cities_choosed_list = []

        while attempt != 5:
            try:
                if villages == "1":
                    if one_citie_in_one_island == "1":
                        if lock_loop == False:
                            bot.find_element_by_id("quickbar_dropdown0").click()
                            cities_query = bot.find_elements_by_class_name("fto_town")
                            cities_checkbox = bot.find_elements_by_class_name("town_checkbox")
                            # adding cities to dictionary
                            for item in cities_query:
                                citie = item.find_element_by_class_name("gp_town_link").text
                                key_citie += 1
                                cities_list[key_citie] = citie
                            # adding cities checkboxes to the list
                            for checkbox in cities_checkbox:
                                key_checkbox += 1
                                cities_checkbox_list[key_checkbox] = checkbox
                            print("Wybierz numer miasta do zbiorow z listy (pamietaj tylko 1 miasto na wyspe!!!): \n",
                                cities_list,'\nJesli nie chcesz podac wiecej miast wpisz: "0"',
                            )
                            while continue_choosing == True:
                                cities_choosed = int(input())
                                if cities_choosed != 0:
                                    cities_choosed_list.append(cities_choosed)
                                elif cities_choosed == 0:
                                    continue_choosing = False
                            cities_choosed_list = list(set(cities_choosed_list))
                            lock_loop = True
                        # get a list of selected user's cities and select them in the panel
                        time.sleep(1)
                        for key in cities_choosed_list:
                            cities_checkbox_list[key].click()
                            time.sleep(1)
                        bot.find_element_by_xpath('//*[@id="fto_claim_button"]').click()
                        time.sleep(1)
                        bot.find_element_by_class_name("btn_confirm").click()
                        time.sleep(time_sleep)
                    elif one_citie_in_one_island == "2":
                        data.more_cities_different_island()
                elif villages == "2":
                    data.one_city()
            except:
                attempt += 1
                print("Error nr.", attempt)

    def exit(self):
        bot = self.bot
        bot.close()

# pipenv shell
# python app.py

data = GrepolisBot("login", "haslo")
villages = input("Posiadasz: \n 1) wiecej miast  2) jedno miasto \n")
if villages == "1":
    one_citie_in_one_island = input("Czy posiadasz miasta na tej samej wyspie? \n 1) Tak  2) Nie \n")
buff = input('Czy masz odblokowana "Lojalnosc Chlopow" ? \n 1) Tak  2) Nie \n')
if buff == "1":
    time_sleep = 60 * 10
elif buff == "2":
    time_sleep = 60 * 5
data.account_login()
data.server_choose()
data.toolbar()
data.village_clicker()
data.exit()