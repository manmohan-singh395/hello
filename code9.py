# import qrcode
# data = 'https://www.hotstar.com/in/home/'

# img = qrcode.make(data)
# img.save('hotstar.jpg')
# print("Qr code generated and save as hotstar.jpg")

# import pyshorteners
# url = 'https://github.com/ganeshdutt100/Python_3pm'
# shortener = pyshorteners.Shortener()
# short_url = shortener.tinyurl.short(url)
# print(short_url)

import pyttsx3

engine = pyttsx3.init()
text = input("enter a text")
engine.say(text)
engine.runAndWait()
