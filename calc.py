'''Running calculator, that calculates (pace, time,long run, vdot, paces for vdot)'''
import os

MENU_TEXT = """\nRunning Calculator
{0}
1. Long run distance calculation.
2. Distance & Time -> Pace.
3. Pace & Distance -> Time.
4. VDOT calculations & Provide paces.
5. Exit
{0}""".format( "=" * 50)

LONGRUN_TEXT = """
Long run is run in comfortable pace,
It maintain your endurance,
According to Jack Daniels program,
run shouldn't last longer than 120 minutes
or shouldn't have more than 25% of weekly training volume.
"""

def cls():
    '''Clear screen depending of os'''
    os.system('cls' if os.name == 'nt' else 'clear')


def string_tempo(pace):
    '''return pace in minutes'''
    tab_pace = pace.split(':')
    minut = int(tab_pace[0])
    sec = float(tab_pace[1]) / 60
    tempo = minut + sec
    return tempo


def print0(number):
    '''add leading 0 to number string, if number is less than 10'''
    if number <= 9:
        return "0%d" % number
    else:
        return "%d" % number

def string_time(time):
    '''return time from string to minutes(float)'''
    tab_time = time.split(':')
    hour = int(tab_time[0]) * 60
    minut = int(tab_time[1])
    sec = float(tab_time[2]) / 60
    time = hour + minut + sec
    return time


def minutes2time(minutes):
    '''convert from minutes to hh:mm:ss and print it out'''
    hours = int(minutes / 60)
    minut = int(minutes % 60)  # reszta z dzielenia przez godzine to minuty
    seconds = (minutes - int(minutes)) * 60
    print "%s:%s:%s" % (print0(hours), print0(minut), print0(seconds))


def pause_end():
    '''control app: wait for input'''
    raw_input("Press any key to back to menu.")


def menu():
    ''' Main function of program, at startup
    it display menu, wait for input and control flow of application'''
    while True:
        cls()
        print MENU_TEXT
        odp = int(raw_input("What do you want to calculate?\n>> "))
        cls()

        if odp == 1:
            print LONGRUN_TEXT
            dystans = float(
                raw_input("How many kilometres do you run in this week?\n>> "))
            dane_tempa = raw_input("What is your long run pace?\n>> ")

            tempo = string_tempo(dane_tempa)
            lsd = (dystans / 4) / (0.75)
            czas = lsd * tempo

            if czas > 120:
                print "Run in comfortable way for 2 hours."
            else:
                print "Your long run in this week should be: %dkm" % lsd
                print "Probably your run will takes: %d minutes" % czas
            
        elif odp == 2:
            print "Distance & Time -> Pace"
            print "=" * 50

            dystans = float(raw_input("Distance[km]: "))
            dane_czas = raw_input("Time[hh:mm:ss]: ")
            czas = string_time(dane_czas)

            pace = czas / dystans
            minutes = int(pace)
            sec = int((pace - minutes) * 60)

            if sec > 9:
                print "\nIf you ran %.2f km in %s, your pace will be %d:%d min/km" % (dystans, dane_czas, minutes, sec)
            else:
                print "\nIf you ran %.2f km in %s, your pace will be %d:0%d min/km" % (dystans, dane_czas, minutes, sec)

        elif odp == 3:
            print "Pace & Distance -> Time"
            print "=" * 50

            dane_tempa = raw_input("Pace[min/km]: ")
            tempo = string_tempo(dane_tempa)
            dystans = float(raw_input("Distance[km]: "))

            czas = tempo * dystans  # wynik w minutach
            minutes2time(czas)

        elif odp == 4:
            from vdot import vdot_calc
            vdot_calc()

        else:
            print "End with Calculations\nSee u later :)."
            exit(0)

        pause_end()

if __name__ == '__main__':
    menu()
