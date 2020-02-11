import pytest

from running_calculator.core.running_index import RunningIndex


class TestRunningIndex:
    analyzer = RunningIndex()

    @pytest.mark.parametrize(
        "target, distance, index", [
            ("00:17:30", "5km", 58),
            ("00:45:44", "10km", 44)
        ]
    )
    def test_nearest(self, target, distance, index):
        assert self.analyzer.nearest(target, distance) == index


