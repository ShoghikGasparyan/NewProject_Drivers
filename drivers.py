import time

since_epoch = time.time()
object_of_time = time.localtime(since_epoch)
current_time = time.asctime(object_of_time)


class Drivers:
    def __init__(self, name, age, license, speed):
        self.name = name
        self.age = age
        self.speed = speed
        self.license = license

    def divers_data(self):
        driver_info = ('\n', current_time,"The traffic has started for all drivers.\n", current_time, "The Driver is:\t", self.name, ", ", self.age, " years old,",
                       self.license, " License: \n", self.name,
                       "'s Car speed at the moment when policeman stopped was: ", str(self.speed), " km/h. \n So the traffic stopped for the all cars, because", self.name, "'s car was stopped.")
        log = open("driving_results_log.txt", "a+", encoding='utf-8')
        driver_info = " ".join(driver_info)
        log.write(driver_info)
        log.close()
