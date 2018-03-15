from Interface import *
from WinButton import *
from KeyChecker import *
import relayCommand
import debug as D

buttons = []

def main():
	D.P("Program started")
	setButtons()
	myInterface = Interface(buttons)
	KeyChecker(buttons).start()
	myInterface.start()
	relayCommand.close()
	print("Main ended")

def setButtons():
	D.P("Setting buttons")
	buttons.append(WinButton(id = 14, relayId = 1, name = "Sala1",
							width = 100, height = 50, x_poz = 15, y_poz = 15, color = "green"))
	buttons.append(WinButton(id = 15, relayId = 2, name = "Sala2",
							width = 100, height = 50, x_poz = 150, y_poz = 15, color = "green"))
	buttons.append(WinButton(id = -1, relayId = 3, name = "Stop\nAlarm",
							width = 100, height = 70, x_poz = 150, y_poz = 200, color = "green"))

if __name__ == "__main__":
	main()
