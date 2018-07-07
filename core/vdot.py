"""Implement VDOT calculation and print training&racing paces
Required files: daniels_table_races.csv & paces.csv"""

import pandas as pd
from core.constants import *

VDOT = pd.read_csv('data/daniels_table_races.csv', delimiter=',', index_col='Params')
PACES_TAB = pd.read_csv('data/paces.csv', delimiter=',', index_col='Params')


def compare_tim_min(time, time_list, distance):
    """Return nearest time from vdot table to time given by user"""
    test = len(time.split(':'))

    if test == 2 and distance <= 7:
        list2 = [float('.'.join(i.split(':'))) for i in time_list]
        time2 = float('.'.join(time.split(':')))
        out = str(min(list2, key=lambda x: abs(x - time2)))
        out = ':'.join(out.split('.'))
        if len(out) == 4:
            out += '0'
        ind = VDOT.iloc[:, distance - 1][VDOT.iloc[:, distance - 1] == out].index.tolist()[0]
        return out, ind
    elif test == 2 and distance > 7:
        print("Error: time must be in format(hh:mm:ss)")
        return "", ""
    elif test == 3 and distance > 7:
        list2 = [int(''.join(i.split(':'))) for i in time_list]
        time2 = int(''.join(time.split(':')))
        out = str(min(list2, key=lambda x: abs(x - time2)))
        out = out[:1] + ':' + out[1:3] + ':' + out[3:]
        ind = VDOT.iloc[:, distance - 1][VDOT.iloc[:, distance - 1] == out].index.tolist()[0]
        return out, ind
    elif test == 3 and distance <= 7:
        print("Error: time must be in format(mm:ss)")
        return "", ""


def vdot_calc():
    # Race time depends on VDOT

    print('{:~^20}'.format('VDOT Table'))
    print("Choose distance:" + DISTANCES)
    distance = int(input("\n>> "))

    dist_dic = {
        1: '1500m',
        2: '1600m',
        3: '3km',
        4: '3200m',
        5: '5km',
        6: '10km',
        7: '15km',
        8: 'HM',
        9: 'M'
    }

    time = input("Provide your time: ")

    time_tab, ind = compare_tim_min(time, VDOT[dist_dic[distance]], distance)
    print("YOUR VDOT IS: ", ind,"\n")
    print('{:~^20}'.format('PACES'))
    print(PACES_TAB.ix[ind].to_frame())
    print("")
    print('{:~^20}'.format('RACING TIMES'))
    print(VDOT.ix[ind].to_frame().T)
    print("")
