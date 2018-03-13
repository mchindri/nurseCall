
from Tkinter import *
import tkFont
import thread
import debug as D

class Interface():
	def __init__(self, buttons):
		D.P("Creating interface")
		self.win = Tk()
		self.myFont = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')
		self.win.title("First GUI")
		self.win.geometry('800x480')
		self.buttons = buttons
		self.addButtons()
	def __del__(self):
		D.P("Deleting Interface")
		self.win.quit()
	def addButtons(self):
		D.P("Adding buttons to interface")
		for i in self.buttons:
			but = Button(self.win, 
				text = i.name,
				font = self.myFont,
				command = i.command,
				bg = i.color)
			i.addReference(but)
			but.pack()
			but.place(x = i.x_poz, y = i.y_poz, height = i.height, width = i.width)		
		self.addExit()
	def exit(self):
		self.win.quit()
	def start(self):
		D.P("Starting win loop")
		self.win.mainloop()
	def addExit(self):
		but = Button(self.win, text="Exit", font=self.myFont,
					command = self.exit)
		but.pack()
		but.place(x = 100, y = 100, height = 50, width = 100)
