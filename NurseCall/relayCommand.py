import serial
import debug as D


#serPort = serial.Serial('/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0', 19200, timeout=1)

serPort = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

def setRelay(id):
	D.P("Setting relay " + str(id) + " ON")
	msg = "relay on " + str(id) + "\n\r"
	serPort.write(msg)
	D.P("Serial sent: " + msg)
def unsetRelay(id):
	D.P("Setting relay " + str(id) + " OFF")
	msg = "relay off " + str(id) + "\n\r"
	serPort.write(msg)
	D.P("Serial sent: " + msg)


def close():
	D.P("Closing serial port")
	serPort.close()
