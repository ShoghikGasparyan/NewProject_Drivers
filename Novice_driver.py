from drivers import *


class Novice_Driver(Drivers):
    def __init__(self, name, age, license, speed_list, speed):
        super().__init__(name, age, license, speed_list, speed)
        self.license = license
        self.speed_list = speed_list

    def speedOfCar(self):
        for self.speed in self.speed_list:
            self.speed_list.append(random.randint(0, 300))
            if self.speed > 60 and self.speed < 90:
                print(self.speed)
                print("The Policeman stopped the Car")
                print(self.speed_list)
                break

    def drive(self):
        if self.speed > 60 and self.speed < 90:
            return True
        else:
            return False
