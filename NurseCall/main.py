from Interface import *
from WinButton import *
from KeyChecker import *
import debug as D

buttons = []

def main():
	D.P("Program started")
	setButtons()
	myInterface = Interface(buttons)
	KeyChecker(buttons).start()
	myInterface.start()
	print("Main ended")

def setButtons():
	D.P("Setting buttons")
	buttons.append(WinButton(id = 14, name = "Sala1",
							width = 100, height = 50, x_poz = 15, y_poz = 15, color = "green"))
	buttons.append(WinButton(id = 15, name = "Sala2",
							width = 100, height = 50, x_poz = 150, y_poz = 15, color = "green"))	

if __name__ == "__main__":
	main()
