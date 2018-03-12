import keyboard

class InputButton(object):
	"""description of class"""
	OFF = 0
	ON = 1
	def __init__(self, id):
		self.buttonID = id
		self.status = self.OFF

	def isPressed(self):
		if self.status == self.OFF:
			return False
		else:
			self.status = self.OFF
			return True

	def activateSwitch(self):
		print("switch" + str(self.buttonID) + " activated")
		self.status = self.ON

	def read(self):
		#print(str(self.buttonID) + " button readed")
		if keyboard.is_pressed(str(self.buttonID)):
			self.activateSwitch()
			while keyboard.is_pressed(str(self.buttonID)):
				pass
