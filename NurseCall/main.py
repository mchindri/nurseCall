from Interface import *
from WinButton import *
from KeyChecker import *
import thread


buttons = []

def main():
	setButtons()

	myInterface = Interface(buttons)
	myInterfaceIsActive = 1
	try:
		thread.start_new_thread(myInterface.run, ())
	except:
		print "Error: unable to start thread"
	KeyChecker(buttons).start()

	#loop
	while myInterfaceIsActive:
		try:
			myInterface
		except NameError:
			myInterfaceIsActive = 0
	print("Main ended")

def setButtons():
	buttons.append(WinButton(id = 1, name = "Sala1",
							width = 100, height = 50, x_poz = 15, y_poz = 15, color = "green"))
	buttons.append(WinButton(id = 2, name = "Sala2",
							width = 100, height = 50, x_poz = 150, y_poz = 15, color = "green"))

	
if __name__ == "__main__":
	main()
