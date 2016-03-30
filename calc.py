from sys import exit

def stringTempo(pace):
	tabPace = pace.split(':')
	minut = int(tabPace[0])
	sec = float(tabPace[1])/60
	tempo = minut + sec
	return tempo

def pauseEnd():
	raw_input("Press any key to exit.")

print "\nRunning Calculator" 
print "=" * 50
print "1. Long run distance calculation."
print "2. Exit."
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
	print "End with Calculations\nThank you :)."
	pauseEnd()
	exit(0)
else:
	exit(0)
