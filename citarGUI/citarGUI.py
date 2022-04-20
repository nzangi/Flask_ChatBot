# importing libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

from tensorflow.keras.models import load_model

model = load_model('Cifar_model_Saved.h5')
classes = {
    0: 'Aeroplane',
    1: 'Automobile',
    2: 'Bird',
    3: 'Cat',
    4: 'Deer',
    5: 'Dog',
    6: 'Frog',
    7: 'Horse',
    8: 'Ship',
    9: 'Truck'
}


def upload_image():
    file_path = filedialog.askopenfile('rb')
    uploaded = Image.open(file_path)
    # uploaded.thumbnail(((top.winfo_width() / 2.25),(top.winfo_height() / 2.25)))

    uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
    im= ImageTk.PhotoImage(uploaded)
    sign_image.configure(image=im)
    sign_image.image = im
    label.configure(text='')
    show_classify_buttom(file_path)


def show_classify_buttom(file_path):
    classify_btn = Button(top, text='Classify Image', command=lambda: classify(file_path), padx=10, pady=5)
    classify_btn.configure(background='#364156', foreground='white', font=('arial', 20, 'bold'))
    classify_btn.place(relx=0.79, rely=0.46)


def classify(file_path):
    image = Image.open(file_path)
    image = image.resize((32, 32))
    image = numpy.expand_dims(image,axis=0)
    image = numpy.heapArray(image)
    prediction = numpy.argmax(model.predict([image])[0], axis=-1)
    # prediction = model.predict_classes([image])[0]
    sign = classes[prediction]
    print(sign)
    label.configure(foreground='#011638', text='The model predicted the above Image as: ' + sign)


# initialize GUI
top = tk.Tk()
# set parameters of GUI
top.geometry('800x800')
top.title("Image Classification")
top.configure(background='#CDCDCD')
# set heading
heading = Label(top, text="Image Classification", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

upload = Button(top, text='Upload Image', command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 20, 'bold'))
upload.pack(side=BOTTOM, pady=50)

# upload Image
sign_image = Label(top)
sign_image.pack(side=BOTTOM, expand=True)

# predicted class
label = Label(top, background='#CDCDCD', font=('arial', 20, 'bold'))
label.pack(side=BOTTOM, expand=True)

top.mainloop()
