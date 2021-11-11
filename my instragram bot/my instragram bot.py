from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        # testing the chrome using chrome driver
        self.driver = webdriver.Firefox()
        self.username = username
        self.driver.maximize_window()
        sleep(1)
        # navigate to the url  of instagram
        self.driver.get("https://www.instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath('//button[@type = "submit"]').click()
        sleep(3)
        # self.driver.find_element_by_xpath().click()
        # self.driver.find_element_by_xpath('//button[text() ="Not Now"]').click()
        # sleep(2)
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()
        sleep(2)
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element_by_xpath('//button[text()="Not Now"]')).click()
        sleep(2)

    def get_followers(self):
        # WebDriverWait(self.driver,10).until(lambda d: d.find_element_by_xpath(f"//a[contains(@href,/{self.username}')]")).click()

        # self.driver.find_element_by_xpath(f"https://www.instagram.com/{username}/")
        self.driver.find_element_by_css_selector(".gmFkV").click()
        sugs = self.driver.find_element_by_css_selector("")
        self.driver.execute('arguments[0].scrollIntoView()', sugs)
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            scroll_box = self.driver.find_element_by_css_selector("li.wo9IH:nth-child(4)")
            sleep(1)
            height = self.driver.execute("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)


my_bot = InstagramBot('muokinzangijr', 'munyoKI284')
my_bot.get_followers()
