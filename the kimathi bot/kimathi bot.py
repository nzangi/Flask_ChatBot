import selenium
from power import my_password,my_usenames
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class Kimathi:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://portal.dkut.ac.ke/site/index")
        sleep(2)
        self.driver.find_element_by_id("userform-email").send_keys(username)
        sleep(1)
        self.driver.find_element_by_id("userform-password").send_keys(password)
        sleep(5)
        self.driver.find_element_by_name("login-button").click()
        sleep(5)
        #loged to daashboard
        # # dashbord tab
        # self.driver.find_element_by_css_selector(".active > a:nth-child(1)").click()
        # sleep(10)
        #Financials tab
        self.driver.find_element_by_css_selector("#w1 > li:nth-child(2) > a:nth-child(1)").click()
        sleep(3)
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 5):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))
            sleep(0.1)
        self.driver.find_element_by_css_selector(".breadcrumb > li:nth-child(1) > a:nth-child(1)")
        #academics tab
        self.driver.find_element_by_css_selector("#w2 > li:nth-child(3) > a:nth-child(1)").click()
        sleep(3)

        #academics pass myList section
        self.driver.find_element_by_css_selector(".btn-success").click()
        sleep(2)
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 5):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            sleep(0)

        #resources tab
        self.driver.find_element_by_css_selector(".breadcrumb > li:nth-child(1) > a:nth-child(1)")
        self.driver.find_element_by_css_selector("#w1 > li:nth-child(4) > a:nth-child(1)").click()
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 5):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            sleep(0.1)

        #noticeboard tab
        self.driver.find_element_by_css_selector("#w1 > li:nth-child(5) > a:nth-child(1)").click()
        for i in range(1, total_height, 5):
            self.driver.execute_script(f"window.scrollTo(0, {i});")
            sleep(0.1)

        sleep(10)
        # staying on the website and the log out
        self.driver.find_element_by_css_selector("button.btn:nth-child(2)").click()


Kimathi(my_usenames,my_password)
