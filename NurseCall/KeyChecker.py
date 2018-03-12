import keyboard
import thread

class KeyChecker(object):
	def __init__(self, buttons):
		self.buttons = buttons
		self.active = 0
	def start(self):
		self.active = 1
		try:
			thread.start_new_thread(self.run, ())
		except:
			print("Running key checker fail")
	def stop(self):
		self.active = 0
	def run(self):
		while self.active == 1:
			for i in self.buttons:
				i.read()