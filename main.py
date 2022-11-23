import random
from drivers import *
from Novice_driver import *
from No_license import *
from Experienced_driver import *

name = input("Name and surname of first driver:\t")
age = int(input("Input age of first driver:\t"))
license = input("Have license - YES OR NO:\t")
speed_list = []
length = 5
while len(speed_list) < length:
    speed_list.append(random.randint(0, 300))

no_license = Drivers(name, age, license, speed_list)
Drivers.divers_data()