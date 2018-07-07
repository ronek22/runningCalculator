from core.utils import *


def long_run(mileage, pace):
    calculated_pace = pace_to_number(pace)
    calculated_distance = (mileage / 4) / (0.75)

    time = int(calculated_distance * calculated_pace)

    if time > 120:
        print("Run in comfortable way for 2 hours.")
    else:
        print("""
        Your long run in this week should be: {0:.2f} km
        Probably your run will takes: {1} minutes
        """.format(calculated_distance, time))


def calc_pace(time, distance):
    time_minutes = time_to_number(time)
    pace = time_minutes / distance
    minutes = int(pace)
    seconds = int((pace - minutes) * 60)

    # TODO: Think about better way to add zero to string
    if seconds > 9:
        print("If you ran {0} km in {1}, your pace will be {2}:{3} min/km".format(distance, time, minutes, seconds))
    else:
        print("\nIf you ran {0:.2f} km in {1}, your pace will be {2}:0{3} min/km".format(distance, time, minutes, seconds))

