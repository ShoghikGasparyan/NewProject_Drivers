from drivers import *


class Novice_Driver(Drivers):
    def __init__(self, name, age, license, speed):
        super().__init__(name, age, license, speed)
        self.license = license
        self.speed = speed

    # Յուրաքանչյուր վարորդի համար գրել պոլիմորֆ մեթոդ՝ վարել, առանց պարամետրերի, որը պետք է
    # վերադարձնի bool արժեք (ոստիկանը կանգնեցրել է – true, ոստիկանը չի կանգնեցրել – false):
    # Սկսնակ վարորդին կկանգնեցնեն եթե նա երթևեկում է [60, 90] արագության միջակայքում:

    def drive(self):
        print("The Novice driver's speed is: ", self.speed, "km/h.")
        if self.speed > 60 and self.speed < 90:

            return True
        else:
            return False
