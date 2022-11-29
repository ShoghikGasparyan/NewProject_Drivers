from drivers import *


class No_License(Drivers):
    def __init__(self, name, age, license, speed):
        super().__init__(name, age, license, speed)
        self.speed = speed

    # Յուրաքանչյուր վարորդի համար գրել պոլիմորֆ մեթոդ՝ վարել, առանց պարամետրերի, որը պետք է
    # վերադարձնի bool արժեք (ոստիկանը կանգնեցրել է – true, ոստիկանը չի կանգնեցրել – false):
    # Վարորդին ով չունի ՎՎ կանգնեցնում են եթե նա երթեևեկում է 60-ից բարձր արագությամբ:

    def drive(self):
        print("The No Licensed driver's speed is: ", self.speed, "km/h.")
        if self.speed > 60:
            return True
        else:
            return False
