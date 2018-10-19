"""Implement VDOT calculation and print training&racing paces
Required files: daniels_table_races.csv & paces.csv"""

import pandas as pd
import os
pd.set_option('display.expand_frame_repr', False)


class RunningIndex:
    def __init__(self):
        self.data_folder = os.path.abspath(os.path.dirname(__file__))
        self.VDOT = self.__prepare_table()
        self.PACES_TAB = pd.read_csv(os.path.join(self.data_folder, '..\data\paces.csv'), delimiter=',', index_col='Params')

    def __prepare_table(self):
        """Read the csv table and convert all time columns to timedelta"""
        timetable = pd.read_csv(os.path.join(self.data_folder, '..\data\daniels_table_races.csv'), delimiter=',', index_col='Params')
        for column in list(timetable):
            timetable[column] = timetable[column].apply(pd.Timedelta)
        return timetable

    def nearest(self, target, distance):
        """Return index(VDOT coefficient) of closest time in given distance"""
        row = min(self.VDOT[distance], key=lambda x: abs(x - target))
        return self.VDOT.loc[self.VDOT[distance] == row].index.item()

    def __print_results(self, ind):
        print("YOUR VDOT IS: ", ind, "\n")
        print('{:~^20}'.format('PACES'))
        print(self.PACES_TAB.ix[ind].to_frame())
        print("")
        print('{:~^20}'.format('RACING TIMES'))
        print(self.VDOT.ix[ind].to_frame().T)
        print("")

    def calculate(self, distance, time):
        coefficient = self.nearest(time, distance)
        self.__print_results(coefficient)

