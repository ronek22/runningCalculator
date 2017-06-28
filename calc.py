from sys import exit
import os
#return pace in minutes
def stringTempo(pace):
	tabPace = pace.split(':')
	minut = int(tabPace[0])
	sec = float(tabPace[1])/60
	tempo = minut + sec
	return tempo

def print0(x):
	if x <= 9:
		return "0%d" % x
	else:
		return "%d" % x

# return time from string to minutes(float)
def stringTime(time):
	tabTime = time.split(':')
	hour = int(tabTime[0])*60
	minut = int(tabTime[1])
	sec = float(tabTime[2])/60
	time = hour + minut + sec
	return time

def minutes2Time(minutes):
	hours = int(minutes/60)
	minut = int(minutes%60) # reszta z dzielenia przez godzine to minuty
	seconds = (minutes - int(minutes))*60
	print "%s:%s:%s" % (print0(hours),print0(minut),print0(seconds))

def pauseEnd():
	raw_input("Press any key to exit.")

print "\nRunning Calculator"
print "=" * 50
print "1. Long run distance calculation."
print "2. Distance & Time -> Pace."
print "3. Pace & Distance -> Time"
print "3. Exit"
print "-" * 50
print "New functions will be added soon.\n"

odp = int(raw_input("What do you want to calculate?\n>> "))

if odp == 1:
	print """
Long run is run in comfortable pace,
It maintain your endurance,
According to Jack Daniels program, run shouldn't last longer than 120 minutes
or shouldn't have more than 25% of weekly training volume.
	"""
	dystans = float(raw_input("How many kilometres do you run in this week?\n>> "))
	daneTempa = raw_input("What is your long run pace?\n>> ")
	tempo = stringTempo(daneTempa)

	s = (dystans/4)/(0.75)
	czas = s*tempo

	if czas > 120:
		print "Run in comfortable way for 2 hours."
		pauseEnd()
		exit(0)
	else:
		print "Your long run in this week should be: %dkm" % s
		print "Probably your run will takes: %d minutes" % czas
		pauseEnd()

elif odp == 2:
	print "Distance & Time -> Pace"
	print "=" * 50
	run = True

	while run :
		os.system('CLS')
		dystans = float(raw_input("Distance[km]: "))
		daneCzas = raw_input("Time[hh:mm:ss]: ")
		czas = stringTime(daneCzas)

		pace = czas/dystans
		minutes = int(pace)
		sec = int((pace - minutes)*60)

		print ""
		if sec > 9:
			print "If you ran %.2f km in %s, your pace will be %d:%d min/km" % (dystans,daneCzas,minutes,sec)
		else:
			print "If you ran %.2f km in %s, your pace will be %d:0%d min/km" % (dystans,daneCzas,minutes,sec)

		test = raw_input("If you want to exit, type T + Enter\n> ")
		if test == 'T':
			run = False

	pauseEnd()
	exit(0)

elif odp == 3:
	print "Pace & Distance -> Time"
	print "=" * 50
	run = True

	while run :
		os.system('CLS')
		daneTempa = raw_input("Pace[min/km]: ")
		tempo = stringTempo(daneTempa)
		dystans = float(raw_input("Distance[km]: "))

		czas = tempo*dystans # wynik w minutach
		minutes2Time(czas)

		test = raw_input("If you want to exit, type T + Enter\n>> ")
		if test == 'T':
			run = False

	# print "Time = %f\n" % czas
	pauseEnd()
	exit(0)


elif odp == 4:
	print "End with Calculations\nSee u later :)."
	pauseEnd()
	exit(0)
else:
	exit(0)