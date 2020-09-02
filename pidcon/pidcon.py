import threading

from events import Events


class PID(Events):
    def __init__(self, kp, ki, kd, sample_rate, n=1):
        self.__events__ = "on_new_output"

        self.__output_timer = threading.Timer(sample_rate, self.calculate_output)
        self.__output_timer.daemon = True

        self.__Kp = kp
        self.__Ki = ki
        self.__Kd = kd
        self.__n = n
        self.__proportional = 0
        self.__integral = 0
        self.__derivative = 0

        self.__sample_rate = sample_rate
        self.__input_error = 0

        self.__is_enabled = False
        self.__last_output = 0

        self.__output_timer.start()

    def calculate_output(self):
        if not self.__is_enabled:
            output = self.__last_output
        else:
            output = self.n * (self.__proportional + self.__integral + self.__derivative)

        self.on_new_output(output)
        self.__last_output = output
        self.__output_timer = threading.Timer(self.__sample_rate, self.calculate_output)
        self.__output_timer.daemon = True
        self.__output_timer.start()

    def enable_pid(self):
        self.__is_enabled = True

    def disable_pid(self):
        self.__is_enabled = False
