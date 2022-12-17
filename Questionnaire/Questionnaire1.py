from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome("/home/nzangi/Downloads/chromedriver_linux64 (1)/chromedriver")
browser.maximize_window()
# for i in range(2):
for i in range(10):
    browser.get("https://forms.gle/XiDQgHVZgY7CcPoKA")
    sleep(2)
    textboxes1 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i8']"))
    sleep(2)
    textboxes1.click()

    textboxes2 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i18']"))
    sleep(2)
    textboxes2.click()

    textboxes3 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div["
                                                                                     "2]/div[3]/div/div/div[2]/div/div["
                                                                                     "1]/div[2]/textarea"))
    textboxes3.click()
    textboxes3.send_keys("May the Limited customer base in the area")
    sleep(2)

    textboxes4 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div["
                                                                                     "2]/div[4]/div/div/div[2]/div/div["
                                                                                     "1]/div[2]/textarea"))
    textboxes4.click()
    textboxes4.send_keys("Cancellation of the orders made due to product unavailability by the seller")
    sleep(2)

    textboxes5= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i39']"))
    sleep(2)
    textboxes5.click()

    textboxes6= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i52']"))
    sleep(3)
    textboxes6.click()

    textboxes7= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i66']"))
    sleep(3)
    textboxes7.click()

    textboxes8= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i72']"))
    sleep(2)
    textboxes8.click()

    textboxes9= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i75']"))
    sleep(2)
    textboxes9.click()
    textboxes10= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i83']"))
    sleep(2)
    textboxes10.click()

    textboxes11= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i89']"))
    sleep(2)
    textboxes11.click()

    textboxes11= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i92']"))
    sleep(2)
    textboxes11.click()

    textboxes111 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i95']"))
    sleep(2)
    textboxes111.click()

    textboxes1111 = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i98']"))
    sleep(2)
    textboxes1111.click()

    #Button
    textboxes12= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i111']/div[3]/div"))
    sleep(2)
    textboxes12.click()

    textboxes13= WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='i118']/div[3]/div"))
    sleep(2)
    textboxes13.click()

    submit = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div"))
    submit.click()
    sleep(2)
    # browser.get("https://docs.google.com/forms/d/e/1FAIpQLSdQtx2aMKCRKjSrq47B2OlZk1o0vOc0mYkDVH3taD3Q4TB5iA/formResponse")
    # submit_submit = WebDriverWait(browser, 11).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"))
    # sleep(2)
    # submit.click()
browser.close()


