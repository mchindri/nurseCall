import serial
import debug as D

#serPort = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

def setRelay(id):
	D.P("Setting relay " + str(id) + " ON")
	#serPort.write("relay ON " + str(id) + "\n\r")
def unsetRelay(id):
	D.P("Setting relay " + str(id) + " OFF")
	#serPort.write("relay OFF " + str(id) + "\n\r")

def close():
	D.P("Closing serial port")
	#serPort.close()