import pyautogui as pt
import emoji
import pyperclip
from pyemojify import emojify
from time import sleep

# # 1136, 736

count = 1
while count <= 300:
    pt.click(1136, 736)
    sleep(0.05)
    pt.write("Si mbaya kutembea. takataka wewe, wacha kunisumbua bana. umezidi sasa")
    sleep(0.05)
    pt.press('enter')
    count += 1
