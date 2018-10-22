"""Script to control user interaction like input and output"""
from .calculator import long_run, calc_pace, calc_time
from .constants import LONG_RUN_TEXT, MENU_TEXT
from .utils import cls, pause_end, get_distance, get_time


def enter_long_run_data():
    """Interact with user to provide long run instructions"""
    print(LONG_RUN_TEXT)

    distance = float(input("How many kilometres do you run in this week?\n>> "))
    pace = input("What is your long run pace?\n>> ")

    print(long_run(distance, pace))


def enter_data_for_pace_calc():
    """Interact with user to calculate pace"""
    print("Distance & Time -> Pace")
    print("=" * 50)

    distance = float(input("Distance[km]: "))
    time = input("Time[hh:mm:ss]: ")

    print(calc_pace(time, distance))


def enter_data_for_time_calc():
    """Interact with user to calculate time"""
    print("Pace & Distance -> Time")
    print("=" * 50)

    pace = input("Pace[min/km]: ")
    distance = float(input("Distance[km]: "))

    calc_time(pace, distance)


def enter_data_to_running_index():
    """Provide data to running index calculate function"""
    print('{:~^20}'.format('VDOT Table'))
    return get_distance(), get_time()


def enter_into_running_index_mode():
    """Interact with user to provide running index data"""
    from .running_index import RunningIndex
    analysis = RunningIndex()
    distance, time = enter_data_to_running_index()
    analysis.calculate(distance, time)


def close_program():
    """Print exit message and close"""
    print("End with Calculations\nSee u later :).")
    exit(0)


def menu():
    """ Main function of program, at startup
    it displays menu, waits for input and controls flow of application"""
    menu_options = [enter_long_run_data, enter_data_for_pace_calc, enter_data_for_time_calc,
                    enter_into_running_index_mode, close_program]
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
