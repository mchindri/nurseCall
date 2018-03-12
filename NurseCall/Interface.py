from Tkinter import *
import tkFont

class Interface():
	def __init__(self, buttons):
		self.win = Tk()
		self.myFont = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')
		self.win.title("First GUI")
		self.win.geometry('800x480')
		self.buttons = buttons
		self.addButtons()
	def __del__(self):
		print("win_deleted")
		self.win.quit()
	def addButtons(self):
		for i in self.buttons:
			but = Button(self.win, 
				text = i.name,
				font = self.myFont,
				command = i.command,
				bg = i.color)
			i.addReference(but)
			but.pack()
			but.place(x = i.x_poz, y = i.y_poz, height = i.height, width = i.width)
	def run(self):
		self.win.mainloop()
	
	def exit(self):
		self.__del__()