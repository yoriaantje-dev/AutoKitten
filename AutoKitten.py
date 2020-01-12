import ctypes
import os
import urllib.request


def get_image(_num):
    print(f"\nLoading kitten background number {_num}\n"
          f"And saving file as 'kitten {_num}.jpg'"
          )
    urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(_num) + ".jpg")
    try:
        os.remove("images/currentKitten.jpg")
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except FileNotFoundError:
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
get_image(number)

abs_path = os.path.abspath("images/currentKitten.jpg")
ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
print("Done, check your desktop ;)")
exit()
