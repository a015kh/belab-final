import serial
import platform
import numpy as np


class EMGDetector:
    def __init__(self, port):
        """
        In windows system COM3 ~ COM8 is possible, check Arduino IDE
        In linux ststem, usually use '/dev/ttyACM0' for UART
        """
        self.ser = serial.Serial(port, 9600, timeout=10)
        self.range = 30
        self.num_record = 30
        self.history = []

    def exec(self):
        s = self.ser.readline().decode().rstrip('\r\n').rstrip('\r\n')
        if len(s) == 0:
            return False
        try:
            value = int(s)
            return self.update(value)
        except ValueError:
            return False

    def update(self, v):
        self.history.append(v)
        if len(self.history) > self.num_record:
            self.history.pop(0)
        if np.std(self.history) > self.range:
            return True
        return False

if __name__ == "__main__":
    detector = EMGDetector("COM7")
    while True:
        detector.exec()
