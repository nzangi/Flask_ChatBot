import time,os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # self.username_twitter = username_twitter
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(2)
        WebDriverWait(bot, 11).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(self.username)
        time.sleep(2)
        bot.find_element_by_css_selector(".r-jwli3a").click()
        # WebDriverWait(bot, 9).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(
        #     self.username_twitter)
        # time.sleep(3)
        # bot.find_element_by_css_selector(".r-jwli3a").click()
        # time.sleep(2)
        WebDriverWait(bot, 13).until(lambda d: d.find_element_by_css_selector(".r-30o5oe")).send_keys(self.password)
        time.sleep(2)
        bot.find_element_by_css_selector(".r-18jsvk2").click()
        time.sleep(1)
        bot.find_element_by_css_selector(".r-y3yin2 > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)").click()
    def like_tweets(self,hashtag):
        bot = self.bot
        # bot.get('https://twitter.com / search?q =% 23'+hashtag+'&src = typed_query&f = live')
        bot.get('https://twitter.com/search?q='+hashtag+'&src=trend_click&vertical=trends')
        time.sleep(3)
        links =set()
        for _ in range(10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(4)
            [
                links.add(elem.get_attribute('href')) for elem in bot.find_elements_by_xpath("//a[@dir ='auto']")
            ]
            print(f'The Links Include:\n{links}')
        for link in links:
            bot.get(link)
            time.sleep(4)

            try:
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="retweet"]'
                ).click()
                actions = ActionChains(bot)
                actions.send_keys(Keys.RETURN).perform()
                bot.find_element_by_css_selector(
                    '.css-18t94o4[data-testid ="like"]'
                ).click()
                time.sleep(15)
            except:
                time.sleep(2)
        bot.get('https://twitter.com/')


my_bot = TwitterBot('@MunyokiMuoki', 'munyoKI284')
my_bot.login()
# @MuokiNzangiJr
hashtag = sys.argv[0]
my_bot.like_tweets(hashtag)
