from random import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from power import my_password, my_usename


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        sleep(5)
        username = WebDriverWait(bot, 13).until(lambda d: d.find_element_by_css_selector(".r-30o5oe"))
        for letter in my_usename:
            username.send_keys(letter)
            sleep(1)

        bot.find_element_by_xpath("").click()

        password = WebDriverWait(bot, 13).until(lambda d: d.find_element_by_css_selector(".r-30o5oe"))
        for letter in my_password:
            password.send_keys(letter)
            sleep(1)

        bot.find_element_by_css_selector(".r-18jsvk2").click()
        # bot.find_element_by_id("login")

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=trend_click&vertical=trends')
        sleep(4)

        bot.find_element_by_link_text('Latest')
        sleep(5)
        total_height = int(self.bot.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 5):
            tweets = bot.find_element_by_xpath("//div[@data-testid='retweet']")
            print(tweets)
            sleep(5)
            bot.find_element_by_xpath("//div[@data-testid='like']").click()

            bot.execute_script(f"window.scrollTo(0, {i});")
            sleep(5)

        # break


my_bot = TwitterBot(my_usename, my_password)
my_bot.login()
my_bot.like_tweets('Eldoret')
