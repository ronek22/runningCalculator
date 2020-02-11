import pytest
from pytest import approx
from datetime import timedelta

from running_calculator.core.utils import pace_to_number, time_to_number, time_to_string, duration


@pytest.mark.parametrize(
    'pace_str, pace_fl', [
        ("3:30", 3.50),
        ("5:00", 5.00),
        ("5:25", 5.41),
        ("6:17", 6.28)
    ]
)
def test_pace_to_number(pace_str, pace_fl):
    assert pace_to_number(pace_str) == approx(pace_fl, rel=1e-2)


@pytest.mark.parametrize(
    'time_str, time_fl', [
        ("00:20:00", 20.00),
        ("00:15:30", 15.50),
        ("01:35:45", 95.75),
        ("00:24:15", 24.25)
    ]
)
def test_time_to_number(time_str, time_fl):
    assert time_to_number(time_str) == approx(time_fl, rel=1e-2)


@pytest.mark.parametrize(
    'badtime_str', [
        "20:00", "30", "00:01:35:20", "24:10"
    ]
)
def test_time_to_number_with_corrupted_input(badtime_str):
    with pytest.raises(ValueError) as error_info:
        time_to_number(badtime_str)
    assert 'to unpack' in str(error_info)


@pytest.mark.parametrize(
    'time_str, time_fl', [
        ("00:20:00", 20.00),
        ("00:15:30", 15.50),
        ("01:35:45", 95.75),
        ("00:24:15", 24.25)
    ]
)
def test_time_to_string(time_str, time_fl, capfd):
    minutes = time_fl
    time_to_string(minutes)
    out, _ = capfd.readouterr()
    assert out == time_str + "\n"


def test_duration():
    assert duration("01:15:25") == timedelta(hours=1, minutes=15, seconds=25)

# modules with input require some complex mocking, so i do it later





