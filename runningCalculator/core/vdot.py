"""Implement VDOT calculation and print training&racing paces
Required files: daniels_table_races.csv & paces.csv"""

import pandas as pd
from datetime import timedelta
from core.constants import DISTANCES, DIST_DIC

pd.set_option('display.expand_frame_repr', False)


def prepare_table():
    """Read the csv table and convert all time columns to timedelta"""
    timetable = pd.read_csv('data/daniels_table_races.csv', delimiter=',', index_col='Params')
    for column in list(timetable):
        timetable[column] = timetable[column].apply(pd.Timedelta)
    return timetable


def duration(time):
    """Convert time from string to timedelta"""
    h, m, s = list(map(int, time.split(":")))
    return timedelta(hours=h, minutes=m, seconds=s)


def nearest(target, distance):
    """Return index(VDOT coefficient) of closest time in given distance"""
    row = min(VDOT[distance], key=lambda x: abs(x - target))
    return VDOT.loc[VDOT[distance] == row].index.item()


VDOT = prepare_table()
PACES_TAB = pd.read_csv('data/paces.csv', delimiter=',', index_col='Params')


def vdot_calc():
    # Race time depends on VDOT

    print('{:~^20}'.format('VDOT Table'))
    print("Choose distance:" + DISTANCES)
    distance = int(input("\n>> "))



    # TODO: ADD SOME VALIDATION
    time = input("Provide your time: ")
    time = duration(time)

    ind = nearest(time, DIST_DIC[distance])

    # time_tab, ind = compare_tim_min(time, VDOT[dist_dic[distance]], distance)
    print("YOUR VDOT IS: ", ind,"\n")
    print('{:~^20}'.format('PACES'))
    print(PACES_TAB.ix[ind].to_frame())
    print("")
    print('{:~^20}'.format('RACING TIMES'))
    print(VDOT.ix[ind].to_frame().T)
    print("")
