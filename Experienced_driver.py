from drivers import *


class Experienced_Driver(Drivers):

    def __init__(self, name, age, license, speed):
        super().__init__(name, age, license, speed)
        self.license = license
        self.speed = speed

    # Յուրաքանչյուր վարորդի համար գրել պոլիմորֆ մեթոդ՝ վարել, առանց պարամետրերի, որը պետք է
    # վերադարձնի bool արժեք (ոստիկանը կանգնեցրել է – true, ոստիկանը չի կանգնեցրել – false):
    # Փորձառու վարորդին կկանգնեցնեն պատահական սկզբունքով, եթե նրա տարիքի և նրա արագության միջին թվաբանականը հավասար լինի
    # պատահական գեներացված թվի:

    def drive(self):
        print("The Experienced driver's speed is: ", self.speed, "km/h.")
        if (int(self.speed) + int(self.age)) / 2 == self.speed:
            return True
        else:
            return False
