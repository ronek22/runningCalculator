import pandas as pd
vdot = pd.read_csv('daniels_table_races.csv',
                   delimiter=',', index_col='Params')
pacesTab = pd.read_csv('paces.csv', delimiter=',', index_col='Params')


def compareTimMin(time, timeList, distance):
    test = len(time.split(':'))

    if test == 2 and distance <= 7:
        list2 = [float('.'.join(i.split(':'))) for i in timeList]
        time2 = float('.'.join(time.split(':')))
        out = str(min(list2, key=lambda x: abs(x - time2)))
        out = ':'.join(out.split('.'))
        if len(out) == 4:
            out += '0'
        ind = vdot.iloc[:, distance - 1][vdot.iloc[:,distance - 1] == out].index.tolist()[0]
        return out, ind
    elif test == 2 and distance > 7:
        print "Error: time must be in format(hh:mm:ss)"
        return "", ""
    elif test == 3 and distance > 7:
        list2 = [int(''.join(i.split(':'))) for i in timeList]
        time2 = int(''.join(time.split(':')))
        out = str(min(list2, key=lambda x: abs(x - time2)))
        out = out[:1] + ':' + out[1:3] + ':' + out[3:]
        ind = vdot.iloc[:, distance - 1][vdot.iloc[:,distance - 1] == out].index.tolist()[0]
        return out, ind
    elif test == 3 and distance <= 7:
        print "Error: time must be in format(mm:ss)"
        return "", ""


def vdotCalc():
    # Race time depends on VDOT

    print '{:~^20}'.format('Vdot Table')
    print "Choose distance:"
    print """
    1. 1500m
    2. 1600m
    3. 3km
    4. 3200m
    5. 5km
    6. 10km
    7. 15km
    8. Half Marathon
    9. Marathon
    """
    distance = int(raw_input("\n>> "))
    distDic = {
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

    time = raw_input("Provide your time: ")

    timeTab, ind = compareTimMin(time, vdot[distDic[distance]], distance)
    # print "NEAREST TIME: ", timeTab
    print "YOUR VDOT IS: ", ind,"\n"
    print '{:~^20}'.format('PACES')
    print pacesTab.ix[ind].to_frame()
    print ""
    print '{:~^20}'.format('RACING TIMES')
    print vdot.ix[ind].to_frame().T
    print ""
