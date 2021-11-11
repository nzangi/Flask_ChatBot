import pyautogui as pt
from time import sleep
import pyperclip
import cv2
import random

sleep(2)
position1 = pt.locateOnScreen("///home/nzangi/PycharmProjects/my projects/whatsapp/whatappimages/smiley_clip.png",
                              confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x, y
    position = pt.locateOnScreen("///home/nzangi/PycharmProjects/my projects/whatsapp/whatappimages/smiley_clip.png",
                                 confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 110, y - 50, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveTo(1189, 433, duration=.5)
    # whatsapp_message = pt.hotkey('ctrl','c' )
    # pt.hotkey('ctrl','v' )
    pt.click()
    sleep(1)
    whatsapp_message = pyperclip.paste()
    print("Message Received: " + whatsapp_message)
    return whatsapp_message


# responding the message
def post_response(message):
    global x, y
    position = pt.locateOnScreen("///home/nzangi/PycharmProjects/my projects/whatsapp/whatappimages/smiley_clip.png",
                                 confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval = .1)


# process the message
def process_response(message):
    random_number = random.randrange(3)
    if ' ? ' in str(message).lower():
        return "Please I am Unable to respond messages for now, ask me later, OK?"
    else:
        if random_number == 0:
            return "That's Cool"
        elif random_number == 1:
            return "My friend, How is the going?"
        else:
            return "Do you want to say anything ? "


def check_new_messages():
    pt.moveTo(1027,680,duration = .5)
    while True:
        #checks for grren button and new messaages
        try:
           position = pt.locateOnScreen("///home/nzangi/PycharmProjects/my projects/whatsapp/whatappimages/greenbox.png", confidence = .7)
           if position is not None:
               pt.moveTo(position)
               pt.moveRel(-50,0)
               pt.click()
               sleep(.5)
               # print("new message detected your Users")
               # break
        except(Exception):
            print("No new messages from your Users")
        if pt.pixelMatchesColor(int(1027), int(680), (0,0,0), tolerance=10):
            print("Its black color")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages for you")
        sleep(5)

check_new_messages()
# get_message()
# processed_message = process_response(get_message())
# post_response(processed_message)
# post_response(get_message())
