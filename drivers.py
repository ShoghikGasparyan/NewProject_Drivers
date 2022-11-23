import time

since_epoch = time.time()
object_of_time = time.localtime(since_epoch)
current_time = time.asctime(object_of_time)


class Drivers:
    def __init__(self, name, surname, age,):
        self.name = name
        self.surname = surname
        self.age = age

    def divers_data(self):
        driver_info = ('\n', current_time, ':\t', 'The Driver is:\t', self.name, " ", self.surname, ", ", self.age, " years old.")
        log = open("driving_results_log.txt", "a+", encoding='utf-8')
        driver_info = "".join(driver_info)
        log.write(driver_info)
        log.close()




