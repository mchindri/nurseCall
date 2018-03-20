import thread
import time
import debug as D

class KeyChecker(object):
	def __init__(self, buttons):
		D.P("Creating Key Checker")
		self.buttons = buttons
		self.active = 0
	def start(self):
		D.P("Starting keychecker thread")
		self.active = 1
		try:
			thread.start_new_thread(self.run, ())
		except:
			D.P("Running key checker fail")
	def stop(self):
		D.P("Stopping key checker")
		self.active = 0
	def run(self):
		while self.active == 1:
			D.P("Key checker is working")
			for i in self.buttons:
				i.read()
			time.sleep(1.0)
