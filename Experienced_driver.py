from drivers import *


class Experienced_Driver(Drivers):

    def __init__(self, name, age, license, speed_list, speed):
        super().__init__(name, age, license, speed_list, speed)
        self.license = license
        self.speed_list = speed_list


    def speedOfCar(self):
        randomNumber = random.randint(0, 300)
        for self.speed in self.speed_list:
            self.speed_list.append(random.randint(0, 300))
            if (int(self.speed) + int(self.age))/2 == randomNumber:
                print(self.speed)
                print("The Policeman stopped the Car")
                print(self.speed_list)
                break

    # def drive(self):
    #     if speedOfCar = True
    #         return True
    #     else:
    #         return False
