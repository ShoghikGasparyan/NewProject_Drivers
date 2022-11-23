from drivers import *
import random

class No_License(Drivers):
    def __init__(self,name, age, license, speed_list):
        super().__init__(name,age, license, speed_list)
        self.license = license
        self.speed_list = speed_list

    def drive(self):
        return True

    if drive():
        print("yes")
    else:
        print("no")

    def speedOfCar(self):
        for speed in self.speed_list:
            self.speed_list.append(random.randint(0, 300))
            if speed > 60:
                print(speed)
                print("stop")
                print(self.speed_list)
                break

