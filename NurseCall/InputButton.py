import keyboard
#import RPi.GPIO as GPIO
import debug as D



class InputButton(object):
	"""description of class"""
	OFF = 0
	ON = 1
	#GPIO.setmode(GPIO.BCM)

	def __init__(self, id):
		self.buttonID = id
		self.inputPin = id
		#GPIO.setup(self.inputPin, GPIO.IN)
		self.status = self.OFF
		#self.addEvent()

	def isPressed(self):
		if self.status == self.OFF:
			return False
		else:
			self.status = self.OFF
			return True

	def activateSwitch(self, pinReaded):
		D.P("Button" + str(self.buttonID) + " activated")
		self.status = self.ON

	def addEvent(self):
		D.P("Setting callback for button " + str(self.buttonID))
		GPIO.add_event_detect(self.buttonID, GPIO.RISING,
								callback = self.activateSwitch) 

'''
	#for GPIO
	def read(self):
		if self.status == self.OFF:
			if GPIO.input(self.inputPin) == True:
				D.P("Button " + str(self.inputPin) + " pressed")
				self.activateSwitch()
'''
'''
	def read(self):
		#print(str(self.buttonID) + " button readed")
		if keyboard.is_pressed(str(self.buttonID)):
			self.activateSwitch()
			while keyboard.is_pressed(str(self.buttonID)):
            	pass
'''
