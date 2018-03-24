from Interface import *
from WinButton import *
from KeyChecker import *
import relayCommand
import debug as D
import time

buttons = []

def main():
	D.P("Program started")
	setButtons()
	myInterface = Interface(buttons)
	kc = KeyChecker(buttons)
	kc.start()
	myInterface.start()

	kc.stop()
	relayCommand.close()
	print("Main ended")

def setButtons():
    
	D.P("Setting buttons")
	buttons.append(WinButton(id = 14, relayId = 3, name = "DORMITOR 1",
							width = 120, height = 120, x_poz = 127, y_poz = 355, color = "green"))
	buttons.append(WinButton(id = 15, relayId = 3, name = "DORMITOR 2",
							width = 120, height = 120, x_poz = 5, y_poz = 355, color = "green"))
	buttons.append(WinButton(id = 12, relayId = 3, name = "BAIE 1",
                                                        width = 80, height = 60, x_poz = 5, y_poz = 290, color = "green"))
	buttons.append(WinButton(id = 13, relayId = 3, name = "BAIE D.3",
                                                        width = 80, height = 60, x_poz = 5, y_poz = 225, color = "green"))
	buttons.append(WinButton(id = 16, relayId = 3, name = "DORMITOR 3",
                                                        width = 120, height = 90, x_poz = 5, y_poz = 135, color = "green"))
	buttons.append(WinButton(id = 17, relayId = 3, name = "DORMITOR 4",
                                                        width = 120, height = 120, x_poz = 127, y_poz = 60, color = "green"))
	buttons.append(WinButton(id = 18, relayId = 3, name = "DORMITOR 5",
                                                        width = 120, height = 120, x_poz = 248, y_poz = 60, color = "green"))
	buttons.append(WinButton(id = 19, relayId = 3, name = "BAIE 2",
                                                        width = 70, height = 70, x_poz = 150, y_poz = 220, color = "green"))
	buttons.append(WinButton(id = 20, relayId = 3, name = "BAIE 3",
                                                        width = 60, height = 80, x_poz = 370, y_poz = 100, color = "green"))
	buttons.append(WinButton(id = 21, relayId = 3, name = "DORMITOR 6",
                                                        width = 120, height = 120, x_poz = 432, y_poz = 60, color = "green"))
	buttons.append(WinButton(id = 22, relayId = 3, name = "DORMITOR 7",
                                                        width = 120, height = 120, x_poz = 553, y_poz = 60, color = "green"))
	buttons.append(WinButton(id = 23, relayId = 3, name = "DORMITOR 8",
                                                        width = 120, height = 90, x_poz = 675, y_poz = 135, color = "green"))
	buttons.append(WinButton(id = 24, relayId = 3, name = "BAIE D.8",
                                                        width = 80, height = 60, x_poz = 715, y_poz = 225, color = "green"))
	buttons.append(WinButton(id = 25, relayId = 3, name = "BAIE 4",
                                                        width = 80, height = 60, x_poz = 715, y_poz = 290, color = "green"))
	buttons.append(WinButton(id = 26, relayId = 3, name = "DORMITOR 9",
                                                        width = 120, height = 120, x_poz = 675, y_poz = 355, color = "green"))
	buttons.append(WinButton(id = 27, relayId = 3, name = "DORMITOR 10",
                                                        width = 120, height = 120, x_poz = 553, y_poz = 355, color = "green"))
	buttons.append(WinButton(id = 28, relayId = 3, name = "BAIE 5",
                                                        width = 70, height = 70, x_poz = 580, y_poz = 220, color = "green"))
	buttons.append(WinButton(id = -1, relayId = 3, name = "Stop\nAlarm",
							width = 100, height = 70, x_poz = 370, y_poz = 355, color = "green"))

if __name__ == "__main__":
	main()
