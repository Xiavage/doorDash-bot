from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from time import sleep


class DashBot:

    def __init__(self, user, password):
        self.user = user
        self.password = password

        self.driver = webdriver.Chrome()

        # open up a chrome window
        self.openWebsite()

    def openWebsite(self):
        self.driver.get("https://doordash.com")
        sleep(10)

        # click the sign in button

        self.driver.find_element_by_class_name("sc-iybRtq").click()

        self.signIn(self.user, self.password)

    # sign in to account
    def signIn(self, user, password):
        # username id
        sleep(2)
        self.driver.find_element_by_id("FieldWrapper-2").send_keys(user)

        # password id
        self.driver.find_element_by_id("FieldWrapper-3").send_keys(password)

        sleep(2)
        # sign in to doordash
        self.driver.find_element_by_xpath(
            "//div[contains(text(),'Sign In')]").click()

# THIS BOT IS FOR PEOPLE THAT HAVE AN ORDER THEY USUALLY GET SO ALL THEY HAVE TO DO IS RUN THE BOT AND ORDER IT. IN MY CASE WE WILL USE WILLIES AS AN EXAMPLE

# give a list of options to eat
        print("Where would you like to eat: ")
        restaurants = ["1. Willies", "2. Popeyes",
                       "3. Torchy's", "4. CFA", "5. Jersey Mikes"]
        print(restaurants)
        num = int(input("Please enter the number you would like to eat at today: "))
        restaurant = restaurants[num-1]
        restaurant = restaurant.split(" ")
        number = restaurant[0]
        number = int(number[0])
        print(number)

        restaurant = restaurant[1]
        x_link = '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/a'

        print(restaurant)
        sleep(10)
        if(number == 1):
            # order from willies
            restaurant = "Willies Grill & Icehouse"
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(restaurant)
            sleep(1)
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(Keys.ENTER)
            sleep(10)
            self.driver.find_element_by_xpath(x_link).click()
            self.willies_order()

        elif(number == 2):
            # order from popeyes
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(restaurant)
            sleep(1)
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(Keys.ENTER)
            sleep(10)
            self.driver.find_element_by_xpath(x_link).click()
            self.popeyes_order()

        elif(number == 3):
            # order from torchys
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(restaurant)
            sleep(1)
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(Keys.ENTER)
            sleep(10)
            self.driver.find_element_by_xpath(x_link).click()
            self.torchy_order()
        elif(number == 4):
            # order from cfa
            restaurant = "Chick fil a"
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(restaurant)
            sleep(1)
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(Keys.ENTER)
            sleep(10)
            self.driver.find_element_by_xpath(x_link).click()
            self.cfa_order()
        else:
            # order from jimmy johns
            restaurant = "Jersey Mikes Subs"
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(restaurant)
            sleep(1)
            self.driver.find_element_by_id(
                "FieldWrapper-2").send_keys(Keys.ENTER)
            sleep(10)
            self.driver.find_element_by_xpath(x_link).click()
            self.jm_order()

    def willies_order(self):
        # country fried steak with loaded fries and mashed potatoes
        print("Willies")
        # checkout

    def popeyes_order(self):
        # popeyes chicken sandwich with fries and hawaiann punch drink
        print("Popeyes!")

    def torchy_order(self):
        # two trailer parks and sometimes queso depends on if they still have $15
        print("Torchys!")

    def cfa_order(self):
        print("CFA!")

        # chicken wrap and nuggets and fries and cfa sauce
    def jm_order(self):
        print("Jersey Mikes!")

        # philly cheese steak with chips


if __name__ == '__main__':
    # ask for doordash username and password
    username = input("Please enter your username/email for doordash: ").strip()
    password = input("Please enter your password for doordash: ").strip()

    bot = DashBot(username, password)
