import ctypes
import datetime
import os
import time
import urllib.request


def get_image(_date):
    print(f"\nLoading kitten background from {_date}\n"
          f"And saving file as 'kitten {_date}.jpg'"
          )
    urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(_date) + ".jpg")
    time.sleep(1)
    try:
        os.remove("images/currentKitten.jpg")
        time.sleep(1)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except FileNotFoundError:
        time.sleep(1.5)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")


print("Welcome to the AutoKitten function!")
date = datetime.date.today()
time.sleep(1)
get_image(date)

time.sleep(1.5)
abs_path = os.path.abspath("images/currentKitten.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
print("Done, check your desktop ;)")
exit()
