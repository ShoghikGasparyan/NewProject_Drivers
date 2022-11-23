from drivers import *
# from Beginner import *
# from Experienced import *
# from NO_license import *

name = input("If you are a Beginner, please input your Name:\t")
surname = input("Please input your surname:\t")
age = input("Please input your age:\t")
beginner_driver = Drivers(name, surname, age)
beginner_driver.divers_data()

name = input("If you are an experienced driver, please input your Name:\t")
surname = input("Please input your surname:\t")
age = input("Please input your age:\t")
experienced_driver = Drivers(name, surname, age)
experienced_driver.divers_data()

name = input("If you have no license, please input your Name:\t")
surname = input("Please input your surname:\t")
age = input("Please input your age:\t")
no_license_driver = Drivers(name, surname, age)
no_license_driver.divers_data()
