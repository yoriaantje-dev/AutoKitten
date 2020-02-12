import ctypes
import datetime
import os
import shutil
import time
import urllib.error
import urllib.request


def select_option(options):
    _opt = -1
    flag2 = True
    while flag2:
        print("\nWhat would you like to do?")
        for num, _opt in options.items():
            print(f"{num}. {_opt}")

        try:
            _opt = float(input("Choose one of the above numbers: "))
        except TypeError:
            print("Please type only numbers!\n")
        except ValueError:
            print("Please type only numbers!\n")

        if _opt != -1 and _opt in options.keys():
            return _opt
        elif _opt not in options.keys():
            print(f"The option {_opt} is not aviable, please try again!")
        else:
            print("Please type only numbers!\n")


def get_image():
    date = datetime.date.today()
    print(f"\nLoading kitten background from {date}\n"
          f"And saving file as 'kitten {date}.jpg'"
          )
    try:  # Download kitten+date.jpg
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(date) + ".jpg")
        time.sleep(1)
    except FileNotFoundError:
        os.mkdir("images/")
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(date) + ".jpg")
        time.sleep(1)
    except urllib.error.URLError:
        print("Something Strange went wrong, do you have an active internetconnection?")

    try:  # Download currentKitten.jpg
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


print("Welcome to the AutoKitten function!")
options_dict = {
    0: "Close program",
    1: "Run the AutoKitten Function and update my background",
    2: "Open the folder with the images",
    3: "Prune all the images from last month",
    4: "Prune all the images in general"
}
opt = select_option(options_dict)

while True:
    if opt == 0:
        print("Sorry to see you go, thanks for using!")
        exit()
    elif opt == 1:
        get_image()
        set_background()
        print("Done, check your desktop ;)")
        exit()
    elif opt == 2:
        os.startfile(os.path.abspath("images/"))
        opt = select_option(options_dict)
    elif opt == 3:
        # TODO: Add pruning on month basis
        print("Not yet implemented, but coming soon!\n")
        opt = select_option(options_dict)
    elif opt == 4:
        confirm = str(input("Are you sure? ")).lower()
        if confirm == "y":
            try:
                shutil.rmtree(os.path.abspath("images/"))
                print("Succesfully removed directory!\n")
            except FileNotFoundError:
                print("Directory is already removed!\n")
        elif confirm == "n":
            print("Okay, glad you cancelled!\n")
            opt = select_option(options_dict)
        else:
            print("Confirmation is wrong, going to main menu\n")
        opt = select_option(options_dict)
    else:
        print("Option not found, showing main menu\n")
        opt = select_option(options_dict)
