# Lab 7: Fuzzing for Input Validation Bugs

## Objective
Use property-based fuzz testing with Hypothesis to discover and fix input-validation bugs in the marathon registration parser.

## Files
- `marathon_registration_parser.py`: hardened application containing the three parser functions.
- `test_marathon_registration_parser.py`: Hypothesis tests and deterministic regression checks.

## Setup
Run these commands from this folder:

```bash
python -m pip install hypothesis pytest
```

## Run the application
```bash
python marathon_registration_parser.py
```

## Run the tests
```bash
python -m pytest -v test_marathon_registration_parser.py
```

## Validation behaviour
- `format_bib_name` returns an empty string for non-string input and otherwise trims, uppercases, and truncates the name to 12 characters.
- `parse_finish_time` accepts H:MM:SS with numeric fields and minute/second values below 60. Invalid input returns `None`.
- `average_split` accepts one or more non-negative whole-number split values. Invalid or empty input returns `None`.

## Required screenshots
1. Original buggy application execution.
2. Hypothesis failures against the original buggy application.
3. Fixed application execution.
4. Passing test output after applying the fixes.

Capture screenshots from your own terminal after running the commands. Do not fabricate test output.

## Deliverables
Submit the fixed Python module, completed test file, and a PDF containing the four screenshots and the reflection answers required by the lab handout.
