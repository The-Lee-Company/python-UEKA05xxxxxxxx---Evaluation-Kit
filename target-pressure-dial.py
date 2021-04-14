"""
Setup a PID loop so that the dial controls the target output pressure.
"""

import serial
import time

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

# set the PID setpoint to the dial
serial_port.write(b"#W12,1\n")

# set dial range to 0-200
serial_port.write(b"#W25,200\n")

# set the PID input to the pressure sensor (analog input 2)
serial_port.write(b"#W13,2\n")

# set the PID proportional coefficient to 10
serial_port.write(b"#W14,10\n")

# set the PID integral coefficient to 100
serial_port.write(b"#W15,100\n")

# set the target pressure to 123
serial_port.write(b"#W23,123\n")

# turn the pump on
serial_port.write(b"#W0,1\n")

# close serial port
serial_port.close()
