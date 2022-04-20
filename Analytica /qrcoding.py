import qrcode
image = qrcode.make("https://www.youtube.com/")
image.save("Youtube.png")


image1 = qrcode.make("This is nzangi")
image1.save("nzangi.png")

image2 = qrcode.make("https://www.twitter.com/")
image2.save('twitter.png')

image3 = qrcode.make("https://www.facebook.com/")
image3.save('facebook.png')

image4 = qrcode.make("https://www.instagram.com/")
image4.save('instagram.png')

image2 = qrcode.make("https://nzangi.github.io/")
image2.save('nzangi porfofolio.png')