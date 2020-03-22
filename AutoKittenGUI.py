# Main Imports
import ctypes
import datetime
import os
import time
import urllib.error
import urllib.request

# Tkinter Imports
try:
    import tkinter
except ModuleNotFoundError:
    pass


def get_image():
    date = datetime.date.today()
    print(f"\nLoading kitten background from {date}\n"
          f"And saving file as 'kitten {date}.jpg'")
    # Download kitten+date.jpg
    try:
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(date) + ".jpg")
        time.sleep(1)
    except FileNotFoundError:
        os.mkdir("images/")
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(date) + ".jpg")
        time.sleep(1)
    except urllib.error.URLError:
        print("Something Strange went wrong, do you have an active internetconnection?")

    # Download currentKitten.jpg
    try:
        os.remove("images/currentKitten.jpg")
        time.sleep(1)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except FileNotFoundError:
        time.sleep(1.5)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except urllib.error.URLError:
        print("Something Strange went wrong, do you have an active internetconnection?")


def set_background():
    time.sleep(1.5)
    abs_path = os.path.abspath("images/currentKitten.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
