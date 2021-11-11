import time, os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys


class TwitterBot:
    def __init__(self, username, username_twitter, password):
        self.username = username
        self.username_twitter = username_twitter
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(5)
        WebDriverWait(bot, 11).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(self.username)
        time.sleep(4)
        bot.find_element_by_css_selector(".r-jwli3a").click()
        WebDriverWait(bot, 11).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(
            self.username_twitter)
        time.sleep(4)
        bot.find_element_by_css_selector(".r-jwli3a").click()
        WebDriverWait(bot, 13).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(self.password)
        time.sleep(4)
        bot.find_element_by_css_selector(".r-18jsvk2").click()
        bot.find_element_by_css_selector("..r-y3yin2").click()

    def like_tweets(self, hashtag):
        bot = self.bot
        # WebDriverWait(bot,0).until(lambda d: d.find_element_by_css_selector("a.css-1dbjc4n:nth-child(2) > div:nth-child(1)")).click()
        bot.get('https://twitter.com/search?q=' + hashtag + '&src=trend_click&vertical=trends')
        time.sleep(4)
        # WebDriverWait(bot,15).until(lambda d: d.get('https://twitter.com/search?q=' + hashtag + '&src=trend_click&vertical=trends'))

        #  click latest tweets from the hastags
        bot.find_element_by_xpath("div.r-6b64d0:nth-child(2) > a:nth-child(1) > div:nth-child(1)").click()
        # bot.find_element_by_css_selector("div.r-6b64d0:nth-child(2) > a:nth-child(1)").click()
        # bot.find_element_by_id('data-testid="trend"')
        time.sleep(4)
        bot.find_element_by_css_selector(".r-1ljd8xs > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
        try:
                    # click like button
                    bot.find_element_by_css_selector(
                        "#id__lqykijya6y > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) "
                        "> svg:nth-child(2)").click()
                    # click like retweet button
                    bot.find_element_by_css_selector(
                        "#id__zmsi3933jtc > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) "
                        "> svg:nth-child(2)").click()
                    time.sleep(10)
        except Exception as ex:
                    time.sleep(30)


my_bot = TwitterBot('@MunyokiMuoki','0706306779','munyoKI284')
my_bot.login()
# , '0706306779'
# my_bot.like_tweets('MPESA')
my_bot.like_tweets('Kenyatta')

