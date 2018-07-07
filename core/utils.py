import os


def pace_to_number(pace):
    """return from pace in string to pace in minutes"""
    minutes, seconds = pace.split(':')
    minutes, seconds = int(minutes), float(seconds) / 60
    return minutes + seconds


def time_to_number(time):
    """return time from string to minutes(float)"""
    hours, minutes, seconds = time.split(':')
    hours, minutes, seconds = int(hours) * 60, int(minutes), float(seconds) / 60
    return hours + minutes + seconds


def time_to_string(time):
    """convert from time in minutes to hh:mm:ss and print it out"""
    hours = int(time / 60)
    minutes = int(time % 60)
    seconds = (time - int(time)) * 60
    print("%02d:%02d:%02d" % (hours, minutes, seconds))


def pause_end():
    """control app: wait for input"""
    input("Press any key to back to menu.")


def cls():
    """Clear screen depending of os"""
    os.system('cls' if os.name == 'nt' else 'clear')
