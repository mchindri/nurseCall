import debug as D

class Blinker(object):
	ON = 1
	OFF = 0
	TIME = 500
	ON_COLOR = "red"
	def __init__(self, win, bref, color):
		self.bref = bref
		self.win = win
		self.color = color
		self.status = self.OFF
		self.active = False
	
	def start(self):
		self.active = True
		self.run()

	def stop(self):
		self.active = False
		self.bref.configure(bg = self.color, activebackground = self.color)

	def run(self):
		if self.status == self.ON:
			self.bref.configure(bg = self.color, activebackground = self.color)
			self.status = self.OFF
		else:
			self.bref.configure(bg = self.ON_COLOR, activebackground = self.ON_COLOR)
			self.status = self.ON
		if self.active == True:
			self.win.after(self.TIME, self.run)
		else:
			self.stop()

		
