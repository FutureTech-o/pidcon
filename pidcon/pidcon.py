import threading


class PID:
    def __init__(self):
        self.output_timer = threading.Timer()
