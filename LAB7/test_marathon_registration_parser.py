from hypothesis import given, strategies as st

from marathon_registration_parser import (
    format_bib_name,
    parse_finish_time,
    average_split,
)


@given(st.text() | st.none())
def test_format_bib_name_no_crash(value):
    try:
        format_bib_name(value)
    except Exception as exc:
        assert False, f"format_bib_name crashed with {value!r}: {exc}"


@given(st.text() | st.none())
def test_parse_finish_time_no_crash(value):
    try:
        parse_finish_time(value)
    except Exception as exc:
        assert False, f"parse_finish_time crashed with {value!r}: {exc}"


@given(st.text() | st.none())
def test_average_split_no_crash(value):
    try:
        average_split(value)
    except Exception as exc:
        assert False, f"average_split crashed with {value!r}: {exc}"


def test_valid_examples():
    assert format_bib_name("Aditya Badde") == "ADITYA BADDE"
    assert parse_finish_time("3:45:10") == 13510
    assert average_split("25 26 24") == 25.0


def test_invalid_examples_are_handled():
    assert format_bib_name(None) == ""
    assert parse_finish_time("3:75:10") is None
    assert parse_finish_time("hello") is None
    assert average_split("") is None
    assert average_split("25 abc 24") is None
