from InputButton import *
import debug as d
class WinButton(object):
	def __init__(self, id, name, width, height, x_poz, y_poz, color):
		self.winRef = None
		self.id = id
		self.name = name
		self.command = self.refresh
		self.width = width
		self.height = height
		self.x_poz = x_poz
		self.y_poz = y_poz
		self.color = color
		self.input = InputButton(self.id)
		self.firstTime = 1

	def addReference(self, winRef):
		self.winRef = winRef

	def changeColor(self):
		if self.color == "green":
			self.color = "red"
		else:
			self.color = "green"

	def read(self):
		#self.input.read()
		if self.input.isPressed() == True:
			self.winRef.configure(bg = "red")

	def refresh(self):
		D.P("Refresh button " + str(self.name))
		if self.winRef != None:
			self.winRef.configure(bg = "green")
