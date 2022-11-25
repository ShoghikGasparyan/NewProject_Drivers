import random
from drivers import *
from Novice_driver import *
from No_license import *
from Experienced_driver import *



name = input("Name and surname of the NO Licensed driver:\t")
age = input("Input the age of driver:\t")
license = "NO"
speed = 0
speed_list = []
length = 5
while len(speed_list) < length:
    speed_list.append(random.randint(0, 300))

no_license = No_License(name, age, license, speed_list, speed)
no_license.speedOfCar()
print(no_license.drive())
no_license.divers_data()



name = input("Name and surname of the Novice driver:\t")
age = input("Input the age of driver:\t")
license = "YES"

speed = 0
speed_list = []
length = 5
while len(speed_list) < length:
    speed_list.append(random.randint(0, 300))

novice_driver = Novice_Driver(name, age, license, speed_list, speed)
novice_driver.speedOfCar()
print(novice_driver.drive())
novice_driver.divers_data()



name = input("Name and surname of the Experienced driver:\t")
age = input("Input the age of driver:\t")
license = "YES"

speed = 0
speed_list = []
length = 5
while len(speed_list) < length:
    speed_list.append(random.randint(0, 300))

experienced_driver = Experienced_Driver(name, age, license, speed_list, speed)
experienced_driver.speedOfCar()
print(experienced_driver.drive())
experienced_driver.divers_data()


