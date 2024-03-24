import serial
import time
import threading
import tkinter as tk

class Form1:
    def __init__(self, root):
        self.root = root
        self.root.title("MyLaserTurret")

        self.watch = None
        self.port = serial.Serial()  # Create a serial port object
        self.last_write_time = time.time()

        self.init_ui()

    def init_ui(self):
        self.root.bind("<Motion>", self.on_mouse_move)

        self.watch = threading.Timer(0, self.start_timer)
        self.watch.start()

        self.port.port = "COM5"  # Set the appropriate COM port
        self.port.baudrate = 9600  # Set the baud rate
        self.port.open()  # Open the serial port

    def start_timer(self):
        if self.watch is not None:
            self.watch.cancel()
        self.watch = threading.Timer(0.015, self.start_timer)
        self.watch.start()

    def on_mouse_move(self, event):
        current_time = time.time()
        if current_time - self.last_write_time >= 0.05:  # Add a delay of 50ms between writes
            self.write_to_port(Point(event.x, event.y))
            self.last_write_time = current_time

    def write_to_port(self, coordinates):
        if self.watch.is_alive():
            self.watch.cancel()

        self.watch = threading.Timer(0.015, self.start_timer)
        self.watch.start()

        x_coord = ((180 - (coordinates.x / (self.root.winfo_width() / 180)))/3)+75
        y_coord = ((coordinates.y / (self.root.winfo_height() / 180))/3)+75

        data = "X{:.0f}Y{:.0f}".format(x_coord, y_coord)
        self.port.write(data.encode())

    def run(self):
        self.root.mainloop()
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    root = tk.Tk()
    app = Form1(root)
    app.run()