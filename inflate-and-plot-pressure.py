"""
Enable and capture the streaming output from the pump.
Drive the pump at 1W for 3 seconds, then plot the captured
pressure output.
"""

import serial
import time
from matplotlib import pyplot as plt

# set up port – replace COM port number with the COM port you are using
serial_port = serial.Serial(port="COM30",
                            baudrate=115200,
                            bytesize=8,
                            timeout=2,
                            stopbits=serial.STOPBITS_ONE)

# turn off data streaming mode
serial_port.write(b"#W2,0\n")
time.sleep(0.1)  # Pause briefly while the driver stops streaming data

# flush the serial port input buffer
serial_port.flush()

# turn the pump off whilst configuring system
serial_port.write(b"#W0,0\n")

# set the pump to manual control mode
serial_port.write(b"#W10,0\n")

# set the drive power input to register 23
serial_port.write(b"#W11,0\n")

# set the drive power set point to 1000 mW
serial_port.write(b"#W23,1000\n")

# turn data streaming mode back on
serial_port.write(b"#W2,1\n")

# turn the pump on
serial_port.write(b"#W0,1\n")


# loop for 3 seconds, capturing the serial port output
start_time = time.time()
pressures = list()

while time.time() - start_time < 3:
    line_from_driver = serial_port.readline()

    # '#S' indicates that the line is a streaming output
    if line_from_driver[0:2] == b"#S":
        pressure = float(line_from_driver[2:].split(b",")[5])
        pressures.append(pressure)


# turn the pump off
serial_port.write(b"#W0,0\n")

# close serial port
serial_port.close()


# plot the captured pressure values
plt.plot(pressures)
plt.show()


