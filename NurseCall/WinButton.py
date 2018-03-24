from InputButton import *
import debug as d
import relayCommand
import alarm

class WinButton(object):
	def __init__(self, id, relayId, name, width, height, x_poz, y_poz, color):
		self.winRef = None
		self.id = id
		self.relayId = relayId
		self.name = name
		self.command = self.refresh
		self.width = width
		self.height = height
		self.x_poz = x_poz
		self.y_poz = y_poz
		self.color = color
		self.input = InputButton(self.id)

	def addReference(self, winRef):
		self.winRef = winRef

	def changeColor(self):
		if self.color == "green":
			self.color = "red"
		else:
			self.color = "green"


	def read(self):
		#self.input.read()
		if self.id != -1:
			if self.input.isPressed() == True:
				alarm.setAlarm()
				self.winRef.configure(bg = "red", activebackground = "red")
				relayCommand.setRelay(self.relayId)
		elif alarm.isAlarmActive() == True:
			self.winRef.configure(bg = "red", activebackground = "red")
			if alarm.isAlarmRunning() == False:
				relayCommand.setRelay(self.relayId)
				alarm.runAlarm()
			
				

	def refresh(self):
		D.P("Refresh button " + str(self.name))
		if self.winRef != None:
			self.winRef.configure(bg = "green", activebackground = "green")
			relayCommand.unsetRelay(self.relayId)
			if self.id == -1:
				alarm.stopAlarm()
