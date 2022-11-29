#Յուրաքանչյուր մարդ ունի իր անունը, տարիքը (տարիներով) և ունի ՎՎ թե ոչ և մեքենայի արագությունը:
#Անունը և ՎՎ լինել/չլինելը պետք է լինի ֆիքսված, իսկ մեքենայի արագության համար գեներացնել պատահական թիվ:
#Վարորդները բաժանվում են երեք խմբի՝ վարորդ ով չունի ՎՎ(Վարորդական վկայական),
#սկսնակ վարորդ(ունի ՎՎ) և փորձառու վարորդ(ունի ՎՎ):


import random
from Novice_driver import *
from No_license import *
from Experienced_driver import *




def logic_of_NoLicense():
    name = input("Name and surname of the NO Licensed driver:\t")
    age = input("Input the age of driver:\t")
    license = "NO"
    speed = random.randint(0, 300)

    no_license = No_License(name, age, license, speed)
    if no_license.drive() is True:
        no_license.divers_data()
        return True
    else:
        return False




def logic_of_Novice():
    name = input("Name and surname of the Novice driver:\t")
    age = input("Input the age of driver:\t")
    license = "YES"
    speed = random.randint(0, 300)

    novice_driver = Novice_Driver(name, age, license, speed)
    if novice_driver.drive() is True:
        novice_driver.divers_data()
        return True
    else:
        return False

def logic_of_Experienced():
    name = input("Name and surname of the Experienced driver:\t")
    age = input("Input the age of driver:\t")
    license = "YES"
    speed = random.randint(0, 300)

    experienced_driver = Experienced_Driver(name, age, license, speed)
    if experienced_driver.drive() is True:
        experienced_driver.divers_data()
        return True
    else:
        return False


def main_logic():

    while True:
        if logic_of_NoLicense() is True:
            break
        if logic_of_Novice() is True:
            break
        if logic_of_Experienced() is True:
            break

main_logic()




