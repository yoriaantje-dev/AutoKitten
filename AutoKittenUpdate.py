import ctypes
import os
import time
import urllib.request


def get_image(_num):
    print(f"\nLoading kitten background number {_num}\n"
          f"And saving file as 'kitten {_num}.jpg'"
          )
    urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(_num) + ".jpg")
    time.sleep(1
               )
    try:
        os.remove("images/currentKitten.jpg")
        time.sleep(1)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except FileNotFoundError:
        time.sleep(1.5)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")


def get_num():
    try:
        num = os.listdir('images/')
        num = (len(num))
    except FileNotFoundError:
        os.mkdir('images/')
        num = os.listdir('images/')
        num = (len(num))
    if num == 0:
        num = 1
    return num


print("Welcome to the AutoKitten function!")
number = get_num()
time.sleep(1)
get_image(number)

time.sleep(1.5)
abs_path = os.path.abspath("images/currentKitten.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
print("Done, check your desktop ;)")
exit()
