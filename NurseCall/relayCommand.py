import serial
import debug as D


serPort = serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1.0', 19200, timeout=1)

#serPort = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

def setRelay(id):
	D.P("Setting relay " + str(id) + " ON")
	msg = "relay ON " + str(id) + "\n\r"
	serPort.write(msg)
	D.P("Serial sent: " + msg)
def unsetRelay(id):
	D.P("Setting relay " + str(id) + " OFF")
	msg = "relay OFF " + str(id) + "\n\r"
	serPort.write(msg)
	D.P("Serial sent: " + msg)


def close():
	D.P("Closing serial port")
	serPort.close()
