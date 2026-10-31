"""Tests that exercise both outcomes of the decision branches."""
import pytest

from marathon_registration import entry_fee, start_wave, finisher_status


@pytest.mark.parametrize(
    "race,age,early,tshirt,expected",
    [
        ("5k", 30, False, False, 500),
        ("10k", 30, True, False, 600),
        ("half", 30, False, True, 1500),
        ("full", 65, True, True, 975),
        ("10k", 64, False, False, 800),
    ],
)
def test_entry_fee_valid_paths(race, age, early, tshirt, expected):
    assert entry_fee(race, age, early, tshirt) == expected


@pytest.mark.parametrize(
    "race,age,message",
    [
        ("unknown", 30, "unknown race"),
        ("5k", 11, "too young"),
        ("half", 17, "too young for this distance"),
        ("full", 16, "too young for this distance"),
    ],
)
def test_entry_fee_rejection_branches(race, age, message):
    with pytest.raises(ValueError, match=message):
        entry_fee(race, age, False, False)


@pytest.mark.parametrize(
    "best_time,race,expected",
    [
        (None, "full", "D"),
        (180, "full", "A"),
        (181, "full", "B"),
        (241, "full", "C"),
        (90, "5k", "A"),
        (91, "5k", "B"),
        (121, "5k", "C"),
    ],
)
def test_start_wave_branches(best_time, race, expected):
    assert start_wave(best_time, race) == expected


@pytest.mark.parametrize(
    "elapsed,race,missed,expected",
    [
        (30, "5k", 1, "DSQ"),
        (90, "5k", 0, "finisher"),
        (91, "5k", 0, "DNF"),
        (180, "half", 0, "finisher"),
        (181, "half", 0, "DNF"),
        (360, "full", 0, "finisher"),
        (361, "full", 0, "DNF"),
        (60, "10k", 0, "finisher"),
    ],
)
def test_finisher_status_branches(elapsed, race, missed, expected):
    assert finisher_status(elapsed, race, missed) == expected
