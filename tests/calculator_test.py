import pytest

from running_calculator.core.calculator import long_run, calc_pace, calc_time


@pytest.mark.parametrize(
    "mileage, pace, out", [
        (50, "05:00", """
        Your long run in this week should be: 16.67 km
        Probably your run will takes: 83 minutes
        """),
        (45, "04:30", """
        Your long run in this week should be: 15.00 km
        Probably your run will takes: 67 minutes
        """),
        (70, "03:50", """
        Your long run in this week should be: 23.33 km
        Probably your run will takes: 89 minutes
        """),
    ]
)
def test_long_run_under120(mileage, pace, out):
    assert long_run(mileage, pace) == out


def test_long_run_above120():
    assert long_run(120, "5:00") == "Run in comfortable way for 2 hours."


def test_calc_pace():
    assert calc_pace("00:20:00", 5) == "If you ran 5.00 km in 00:20:00, your pace will be 4:00 min/km"


def test_calc_pace_with_added_zero():
    assert calc_pace("00:35:00", 10) == "If you ran 10.00 km in 00:35:00, your pace will be 3:30 min/km"


def test_calc_time(capfd):
    calc_time("03:30", 10)
    out, err = capfd.readouterr()
    assert out == "00:35:00\n"
