# Launchpad MIDI Analyzer
# Run this python script in interactive mode with the command: python -i LP_Analyzer

from pyo import *

# Query for MIDI device number.
if sys.version_info[0] < 3:
    input = raw_input
pm_list_devices()
num = eval(input("Enter the device number (at left) for Launchpad IN : "))

s = Server()
s.setMidiInputDevice(num)
s.boot().start()

# This function takes MIDI input from the Launchpad and outputs three pieces of useful info:
# RAW MIDI Input - the original incoming note value
# Adjusted MIDI - note value corrected to remove gaps in the sequence as rows increment (Novation programmed it weirdly)
# Coordinate - a coordinate value compatible with the monome grid format. Very useful for interface mapping (i.e. assigning sequencers to rows or columns or all other kinds of fun stuff).

def Note_On_Calc(i):
	pit = notes["pitch"].get(True)[i]
	vel = notes["velocity"].get(True)[i]
	if (15 < int(pit) < 24):
		adjust_note = pit - 8
		x = pit - 16
		y = 1
	elif (31 < int(pit) < 40):
		adjust_note = pit - 16
		x = pit - 32
		y = 2
	elif (47 < int(pit) < 56):
		adjust_note = pit - 24
		x = pit - 48
		y = 3
	elif (63 < int(pit) < 72):
		adjust_note = pit - 32
		x = pit - 64
		y = 4
	elif (79 < int(pit) < 88):
		adjust_note = pit - 40
		x = pit - 80
		y = 5
	elif (95 < int(pit) < 104):
		adjust_note = pit - 48
		x = pit - 96
		y = 6
	elif (111 < int(pit) < 120):
		adjust_note = pit - 56
		x = pit - 112
		y = 7
	else:
		adjust_note = pit
		x = pit
		y = 0
	adjust_note = int(adjust_note)
	x = int(x)
	print ("Raw MIDI Input", pit)
	print ("Adjusted MIDI", adjust_note)
	print ("Coordinate", x, y)

print ("Press buttons in the grid...")

# Receive incoming MIDI notes from launchpad.
notes = Notein(poly=1)
notes.setStealing(True)

# incoming MIDI note triggers callback function for analysis of pitch data
tfon = TrigFunc(notes["trigon"], Note_On_Calc, 0)


