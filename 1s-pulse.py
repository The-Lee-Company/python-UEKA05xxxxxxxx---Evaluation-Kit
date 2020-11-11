import serial
import time

# set up port – replace COM port number with the COM port you are using
serialPort = serial.Serial(port="COM1", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

# turn off data streaming mode
serialPort.write(b"#W2,0\n")

#turn the pump off whilst configuring system
serialPort.write(b"#W0,0\n")

# set the pump to manual control mode
serialPort.write(b"#W10,0\n")

# set the drive power input to register 23
serialPort.write(b"#W11,0\n")

# set the drive power set point to 1000 mW
serialPort.write(b"#W23,1000\n")

# turn the pump on
serialPort.write(b"#W0,1\n")

# wait for 1 second
time.sleep(1)

# set the drive power set point to 1000 mW
serialPort.write(b"#W23,0\n")

# turn the pump off
serialPort.write(b"#W0,0\n")

# close serial port
serialPort.close()
