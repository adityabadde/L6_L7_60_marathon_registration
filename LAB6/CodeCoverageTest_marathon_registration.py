"""Tests focused on executing every statement in marathon_registration.py."""
import pytest

from marathon_registration import entry_fee, start_wave, finisher_status


def test_entry_fee_for_each_race():
    assert entry_fee("5k", 30, False, False) == 500
    assert entry_fee("10k", 30, False, False) == 800
    assert entry_fee("half", 30, False, False) == 1200
    assert entry_fee("full", 30, False, False) == 1800


def test_entry_fee_adjustments():
    assert entry_fee("10k", 30, True, False) == 600
    assert entry_fee("10k", 65, False, False) == 400
    assert entry_fee("10k", 30, False, True) == 1100
    assert entry_fee("10k", 65, True, True) == 600


def test_entry_fee_rejects_invalid_race_and_age():
    with pytest.raises(ValueError, match="unknown race"):
        entry_fee("ultra", 30, False, False)
    with pytest.raises(ValueError, match="too young"):
        entry_fee("5k", 11, False, False)
    with pytest.raises(ValueError, match="too young for this distance"):
        entry_fee("half", 17, False, False)


def test_start_wave_all_outcomes():
    assert start_wave(None, "full") == "D"
    assert start_wave(170, "full") == "A"
    assert start_wave(200, "full") == "B"
    assert start_wave(250, "full") == "C"
    assert start_wave(80, "5k") == "A"
    assert start_wave(100, "5k") == "B"
    assert start_wave(130, "5k") == "C"


def test_finisher_status_all_race_types_and_outcomes():
    assert finisher_status(90, "5k", 0) == "finisher"
    assert finisher_status(91, "5k", 0) == "DNF"
    assert finisher_status(180, "half", 0) == "finisher"
    assert finisher_status(181, "half", 0) == "DNF"
    assert finisher_status(360, "full", 0) == "finisher"
    assert finisher_status(361, "full", 0) == "DNF"
    assert finisher_status(30, "5k", 1) == "DSQ"
