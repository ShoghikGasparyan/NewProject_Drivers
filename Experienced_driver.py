from drivers import *


class Experienced_Driver(Drivers):
    def __init__(self, name, age, license, speed_list):
        super().__init__(name, age, license, speed_list)
        self.license = license
        self.speed_list = speed_list

    def drive(self):
        return True

    if drive():
        print("yes")
    else:
        print("no")