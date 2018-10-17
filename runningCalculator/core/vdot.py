"""Implement VDOT calculation and print training&racing paces
Required files: daniels_table_races.csv & paces.csv"""

import pandas as pd
from core.utils import get_distance, get_time

pd.set_option('display.expand_frame_repr', False)


def prepare_table():
    """Read the csv table and convert all time columns to timedelta"""
    timetable = pd.read_csv('data/daniels_table_races.csv', delimiter=',', index_col='Params')
    for column in list(timetable):
        timetable[column] = timetable[column].apply(pd.Timedelta)
    return timetable


def nearest(target, distance):
    """Return index(VDOT coefficient) of closest time in given distance"""
    row = min(VDOT[distance], key=lambda x: abs(x - target))
    return VDOT.loc[VDOT[distance] == row].index.item()


def print_results(ind):
    print("YOUR VDOT IS: ", ind, "\n")
    print('{:~^20}'.format('PACES'))
    print(PACES_TAB.ix[ind].to_frame())
    print("")
    print('{:~^20}'.format('RACING TIMES'))
    print(VDOT.ix[ind].to_frame().T)
    print("")


VDOT = prepare_table()
PACES_TAB = pd.read_csv('data/paces.csv', delimiter=',', index_col='Params')


def vdot_calc():
    print('{:~^20}'.format('VDOT Table'))

    distance = get_distance()
    time = get_time()
    coefficient = nearest(time, distance)

    print_results(coefficient)

