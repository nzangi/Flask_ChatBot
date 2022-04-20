import turtle
from time import sleep
my_pen = turtle.Turtle()

def curve():
    for i in range(200):
        my_pen.right(1)
        my_pen.forward(1)
def my_heart():
    my_pen.fillcolor('green')
    my_pen.begin_fill()
    my_pen.left(120)
    my_pen.forward(112)
    curve()
    my_pen.left(120)
    curve()
    my_pen.forward(112)
    my_pen.end_fill()

def text():
    my_pen.up()
    my_pen.setpos(-68,95)
    my_pen.down()
    my_pen.color('lightgreen')
    my_pen.write("    HEART",font = ('Verdana', 12,"bold"))

my_heart()
text()
my_pen.ht()
turtle.done()
# sleep(10)




