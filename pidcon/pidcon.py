import threading
import time

from events import Events


class PID(Events):
    def __init__(self, sample_rate, kp=0.0, ki=0.0, kd=0.0, n=1.0):
        super().__init__("on_new_output")

        self._output_timer = threading.Timer(sample_rate, self.calculate_output)
        self._output_timer.daemon = True

        self._kp = kp
        self._ki = ki
        self._kd = kd
        self._n = n
        self._is_enabled = False
        self._input_error = 0.0
        self._sample_rate = sample_rate

        self._proportional = 0.0
        self._integral = 0.0
        self._derivative = 0.0
        self._last_output = 0.0
        self._last_time = time.monotonic()
        self._output_timer.start()

    def calculate_output(self):
        if not self._is_enabled:
            output = self._last_output
        else:
            self._proportional = self._kp * self._input_error
            output = self._n * (self._proportional + self._integral + self._derivative)

        self.on_new_output(output)
        self._last_output = output
        self._output_timer = threading.Timer(self._sample_rate, self.calculate_output)
        self._output_timer.daemon = True
        self._output_timer.start()

    @property
    def is_enabled(self):
        return self._is_enabled

    def enable_pid(self):
        self._is_enabled = True

    def disable_pid(self):
        self._is_enabled = False

    @property
    def kp(self):
        return self._kp

    @kp.setter
    def kp(self, value):
        self._kp = float(value)

    @property
    def ki(self):
        return self._ki

    @ki.setter
    def ki(self, value):
        self._ki = float(value)

    @property
    def kd(self):
        return self._kd

    @kd.setter
    def kd(self, value):
        self._kd = float(value)

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = float(value)

    @property
    def input_error(self):
        return self._input_error

    @input_error.setter
    def input_error(self, value):
        self._input_error = value

    @property
    def sample_rate(self):
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, value):
        self._sample_rate = value
