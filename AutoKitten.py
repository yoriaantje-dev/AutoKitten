import ctypes
import datetime
import os
import time
import urllib.request


def select_option(options):
    if isinstance(options, (int, float)):
        opt = -1
        try:
            opt = int(input("Kies een van de bovenstaande nummers: "))
        except TypeError:
            print("Je moet wel een nummer invoeren!")
        except ValueError:
            print("Je moet wel een nummer invoeren!")
        if opt in range(1, (options + 1)):
            return opt
        else:
            print(f"Keuze {opt} is niet beschikbaar! Probeer het opnieuw!")
    else:
        _opt = -1
        flag2 = True
        while flag2:
            print("\nWat wil je graag doen?")
            for num, _opt in options.items():
                print(f"{num}. {_opt}")

            try:
                _opt = float(input("Kies een van de bovenstaande opties: "))
            except TypeError:
                print("Voer AUB een nummer in!\n")
            except ValueError:
                print("Voer AUB een nummer in!\n")

            if _opt != -1 and _opt in options.keys():
                return _opt
            elif _opt not in options.keys():
                print(f"Keuze {_opt} is niet beschikbaar! Probeer het opnieuw!")
            else:
                print("Voer AUB een nummer in!\n")


def get_image():
    date = datetime.date.today()
    print(f"\nLoading kitten background from {date}\n"
          f"And saving file as 'kitten {date}.jpg'"
          )
    urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/kitten " + str(date) + ".jpg")
    time.sleep(1)
    try:
        os.remove("images/currentKitten.jpg")
        time.sleep(1)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")
    except FileNotFoundError:
        time.sleep(1.5)
        urllib.request.urlretrieve("https://placekitten.com/1920/1080", "images/currentKitten.jpg")


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
    elif opt == 1:
        get_image()
        set_background()
        print("Done, check your desktop ;)")
        exit()
    elif opt == 2:
        os.startfile(os.path.abspath("images/"))
        opt = select_option(options_dict)
    elif opt == 3:
        print("Not yet implemented, but coming soon\n!")
        opt = select_option(options_dict)
    elif opt == 4:
        confirm = str(int("Are you sure? "))
        if confirm == "y":
            os.removedirs(os.path.abspath("images/"))
        elif confirm == "n":
            print("Okay, glad you cancelled!\n")
            opt = select_option(options_dict)
        else:
            print("Confirmation is wrong, going to main menu\n")
            opt = select_option(options_dict)
    else:
        print("Option not found, showing main menu\n")
        opt = select_option(options_dict)
