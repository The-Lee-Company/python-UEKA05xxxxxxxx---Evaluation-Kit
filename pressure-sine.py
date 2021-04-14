"""
Setup a PID loop on the driver board to control the output pressure. Then
send a sequence of target pressures to the board so that the output pressure
follows a sine-wave.
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

# set the pump to PID control mode
serial_port.write(b"#W10,1\n")

# set the PID setpoint to register 23
serial_port.write(b"#W12,0\n")

# set the PID input to the pressure sensor (analog input 2)
serial_port.write(b"#W13,2\n")

# set the PID proportional coefficient to 50
serial_port.write(b"#W14,10\n")

# set the PID integral coefficient to 100
serial_port.write(b"#W15,10\n")

# turn the pump on
serial_port.write(b"#W0,1\n")

# Create a sine-wave, from 0->100
sine_wave = ((math.sin(i * math.pi / 10) + 1) * 50
             for i in range(95))

# Send sine-wave to the driver
for target_pressure in sine_wave:
    serial_port.write(b"#W23,%d\n" % target_pressure)  # Update target power
    time.sleep(0.025)  # Pause 25ms between updates

# turn the pump off
serial_port.write(b"#W0,0\n")

# close serial port
serial_port.close()
