import debug as D
alarmActive = False
alarmRunning = False

def setAlarm():
	D.P("Activating alarm")
	global alarmActive
	alarmActive = True

def isAlarmActive():
	global alarmActive
	return alarmActive

def isAlarmRunning():
	global alarmRunning
	return alarmRunning

def runAlarm():
	D.P("Running alarm")
	global alarmRunning
	alarmRunning = True

def stopAlarm():
	D.P("Stopping alarm")
	global alarmActive
	global alarmRunning
	alarmActive = False
	alarmRunning = False
