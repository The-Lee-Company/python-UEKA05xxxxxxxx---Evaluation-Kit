"""
Send a sequence of target powers to the driver, so that its power output
follows a sine-wave
"""

import serial
import time
import math

# set up port – replace COM port number with the COM port you are using
serial_port = serial.Serial(port="COM30",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)

# turn off data streaming mode
serial_port.write(b"#W2,0\n")

# turn the pump off whilst configuring system
serial_port.write(b"#W0,0\n")

# set the pump to manual control mode
serial_port.write(b"#W10,0\n")

# set the drive power input to register 23
serial_port.write(b"#W11,0\n")

# set the drive power set point to 0 mW
serial_port.write(b"#W23,0\n")

# turn the pump on
serial_port.write(b"#W0,1\n")

# Create a sine-wave
sine_wave = ((math.sin(i * math.pi / 10) + 1) * 500
             for i in range(95))

# Send sine-wave to the driver
for target_power in sine_wave:
    serial_port.write(b"#W23,%d\n" % target_power)  # Update target power
    time.sleep(0.025)  # Pause 25ms between updates

# turn the pump off
serial_port.write(b"#W0,0\n")

# close serial port
serial_port.close()
