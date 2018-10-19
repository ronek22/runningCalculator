from .utils import time_to_number, time_to_string, pace_to_number


def long_run(mileage, pace):
    calculated_pace = pace_to_number(pace)
    calculated_distance = (mileage / 4) / (0.75)

    time = int(calculated_distance * calculated_pace)

    if time > 120:
        return "Run in comfortable way for 2 hours."
    else:
        return ("""
        Your long run in this week should be: {0:.2f} km
        Probably your run will takes: {1} minutes
        """.format(calculated_distance, time))


def calc_pace(time, distance):
    pace = time_to_number(time) / distance
    minutes = int(pace)
    seconds = int((pace - minutes) * 60)

    if seconds > 9:
        return "If you ran {0:.2f} km in {1}, your pace will be {2}:{3} min/km".format(distance, time, minutes, seconds)
    else:
        return "If you ran {0:.2f} km in {1}, your pace will be {2}:0{3} min/km".format(distance, time, minutes, seconds)


def calc_time(pace, distance):
    return time_to_string(pace_to_number(pace) * distance)
