import pyautogui as pt
from time import sleep
#1189,433
# 1027,680
while True:
    posXY = pt.position()
    print(posXY, pt.pixel(posXY[0], posXY[1]))
    sleep(1)
    if posXY[0] == 0:
        break
