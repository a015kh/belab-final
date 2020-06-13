import serial
import numpy as np


class EMGDetector:
    def __init__(self, port):
        """
        In windows system COM3 ~ COM8 is possible, check Arduino IDE
        In linux ststem, usually use '/dev/ttyACM0' for UART
        """
        self.ser = serial.Serial(port, 9600, timeout=10)
        self.range = 20
        self.num_record = 30
        self.history = []
        self.setup_time = 50
        for _ in range(self.setup_time):
            self.exec()

    def exec(self):
        s = self.ser.readline().decode().rstrip('\r\n').rstrip('\r\n')
        if len(s) == 0:
            return False
        try:
            value = float(s)
            if value > self.range:
                return True
        except ValueError:
            pass
        return False

if __name__ == "__main__":
    detector = EMGDetector("COM7")
    while True:
        print(detector.exec())
