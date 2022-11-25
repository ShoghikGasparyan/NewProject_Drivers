from drivers import Drivers
import random



class No_License(Drivers):
    def __init__(self, name, age, license, speed_list, speed):
        super().__init__(name, age, license, speed_list, speed)
        self.name = name


    def speedOfCar(self):
        for self.speed in self.speed_list:
            self.speed_list.append(random.randint(0, 300))
            if self.speed > 60:
                print("The speed of the No Licensed Car is: ", self.speed, " km/h")
                print("The Policeman stopped the Car")
                # print(self.speed_list)
                break

    def drive(self):
        if self.speed > 60:
            return True
        else:
            return False