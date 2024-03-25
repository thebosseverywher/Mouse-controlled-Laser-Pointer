# Mouse-controlled-Laser-Pointer

This repository contains code for a laser turret control system implemented using Python and Arduino. The system allows users to control the movement of a laser turret using a graphical user interface (GUI) on their laptop. The GUI captures the mouse pointer coordinates and converts them into angles for servo motors, which in turn control the movement of the laser turret.

## Features

- Graphical User Interface (GUI) for controlling the laser turret.
- Python code to capture mouse pointer coordinates and convert them into servo angles.
- Arduino code to receive servo angles and control the servo motors accordingly.
- Serial communication between Python and Arduino.

## Requirements

To run this project, you will need the following materials:

- Laptop with Python installed (with pyserial library).
- Arduino Uno.
- 2 servo motors.
- 1 laser diode.

## Setup Instructions

1. **Hardware Setup:**
   - Connect the servo motors and laser diode to the Arduino Uno according to the circuit diagram provided.

2. **Software Setup:**
   - Upload the `laser_turret.ino` sketch to your Arduino Uno.
   - Install the required Python libraries using pip:
     ```
     pip install pyserial
     ```



## License

This project is licensed under the [GPU General Public License v3.0](LICENSE).
