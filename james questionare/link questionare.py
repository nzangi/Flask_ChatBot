from selenium import webdriver
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

browser = webdriver.Chrome()
browser.maximize_window()
for i in range(2):
    browser.get("https://docs.google.com/forms/d/e/1FAIpQLScWDdUFem63nfrYLqg8jeGcMBkicobIiRdNPwqbr5iKEk9uww/viewform")

    sleep(5)
    textboxes1 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_id("i10"))
    textboxes1.click()

    textboxes2 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_id("i20"))
    textboxes2.click()

    textboxes3 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_id("i33"))
    textboxes3.click()

    textboxes4 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_css_selector(
        "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(5) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"))
    textboxes4.send_keys("Advantages \n :", "Ease of use \n", "Mobile Benefits  \n", "Diasvantages \n", " cost acess")

    textboxes5 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_css_selector(
        "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(6) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea"))
    textboxes5.send_keys(
        "IPv6 will have a big place in 5G, primarily because of the Internet of Things (IoT), which will add billions of new devices to this mobile network as it’s roll out. IPv4 cannot cope with the n of unique IP addresses that will be required, but IPv6 can. IPv6 also introduces the Neighbor Discovery Protocol (NDP) that enables multi-protocol interoperability between IoT devices. ")

    textboxes5 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_css_selector(
        "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(7) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input"))

    textboxes5.send_keys(
        "MNOs could deploy their own VoIP applications (to replace VoLTE) giving them a guaranteed level of quality of service using network slicing, and by taking advantage of the much lower latency of 5G networks.")

    textboxes5 = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_css_selector(
        "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(8) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPapertextareaMainContent.exportContent > div.quantumWizTextinputPapertextareaContentArea.exportContentArea > textarea"))

    textboxes5.send_keys("5G Will Need Fiber, and Lots of It,  anytime.")

    submit = WebDriverWait(browser, 11).until(lambda d: d.find_element_by_css_selector(
        "#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress.hasClearButton > div.freebirdFormviewerViewNavigationLeftButtons > div > span > span"))
    submit.click()
