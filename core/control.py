from core.calculator import *
from core.constants import *


def enter_long_run_data():
    print(LONG_RUN_TEXT)

    distance = float(input("How many kilometres do you run in this week?\n>> "))
    pace = input("What is your long run pace?\n>> ")

    long_run(distance, pace)


def enter_data_for_pace_calc():
    print("Distance & Time -> Pace")
    print("=" * 50)

    distance = float(input("Distance[km]: "))
    time = input("Time[hh:mm:ss]: ")

    calc_pace(time, distance)


def enter_data_for_time_calc():
    print("Pace & Distance -> Time")
    print("=" * 50)

    pace = input("Pace[min/km]: ")
    distance = float(input("Distance[km]: "))

    calc_time(pace, distance)


def enter_into_vdot_mode():
    from core.vdot import vdot_calc
    vdot_calc()


def close_program():
    print("End with Calculations\nSee u later :).")
    exit(0)


def menu():
    """ Main function of program, at startup
    it displays menu, waits for input and controls flow of application"""
    menu_options = [enter_long_run_data, enter_data_for_pace_calc, enter_data_for_time_calc, enter_into_vdot_mode,
                    close_program]
    while True:
        cls()
        print(MENU_TEXT)
        choose = int(input("What do you want to calculate?\n>> "))
        cls()

        if 1 <= choose <= 5:
            menu_options[choose-1]()
        else:
            print("That option doesnt exist. Try again.")

        pause_end()
