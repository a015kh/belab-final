import serial
import numpy as np
import time


class EMGDetector:
    def __init__(self, port):
        """
        In windows system COM3 ~ COM8 is possible, check Arduino IDE
        In linux ststem, usually use '/dev/ttyACM0' for UART
        """
        self.ser = serial.Serial(port, 9600, timeout=0.1)
        self.range = 25
        self.num_record = 30
        self.history = 0
        self.setup = 10
        for _ in range(self.setup):
            self.exec()

    def exec(self):
        while True:
            try:
                self.ser.write("s".encode())
                s = self.ser.readline().decode().rstrip('\r\n').rstrip('\r\n')
                if len(s) == 0:
                    return False
                value = float(s)
                print(value)
                if value > self.range:
                    return True
                return False
            except UnicodeDecodeError:
                pass

if __name__ == "__main__":
    detector = EMGDetector("/dev/ttyACM0")
    while True:
        time.sleep(1.5)
        print(detector.exec())

