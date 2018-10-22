"""Script for storing constants variables"""
MENU_TEXT = """\nRunning Calculator
{0}
1. Long run distance calculation.
2. Distance & Time -> Pace.
3. Pace & Distance -> Time.
4. VDOT calculations & Provide paces.
5. Exit
{0}""".format("=" * 50)

LONG_RUN_TEXT = """
Long run is run in comfortable pace,
It maintain your endurance,
According to Jack Daniels program,
run shouldn't last longer than 120 minutes
or shouldn't have more than 25% of weekly training volume.
"""

DISTANCES = """
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

DIST_DIC = {
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
