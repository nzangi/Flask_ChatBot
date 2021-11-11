from selenium import webdriver
from power import my_password, my_username
from time import sleep


class Gmail:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def gmail_login(self):
        driver = self.driver
        driver.get(
            "https://accounts.google.com/signin/v2/identifier?service=CPanel&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        driver.find_element_by_id("identifierId").send_keys(self.username)
        sleep(4)
        driver.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ").click()
        password = driver.find_element_by_name("password")
        password.clear()
        password.send_keys(self.password)
        driver.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(3)").click()


my_bot = Gmail(my_username, my_password)
my_bot.gmail_login()
