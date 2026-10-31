# L6_L7_60 — Marathon Registration

Lab 6: Code and Branch Coverage

## About
A small Python module that works out race entry fees by distance, age and early-bird booking, assigns runners to a start wave and decides each runner's finishing status.

## Files
| File | Description |
|------|-------------|
| `marathon_registration.py` | Application module under test |
| `test_marathon_registration.py` | Original starter test file |
| `CodeCoverageTest_marathon_registration.py` | Test cases for line/code coverage |
| `BranchCoverageTest_marathon_registration.py` | Test cases for decision branch coverage |

## Run the coverage tests
Run these commands from the `LAB6` directory after installing the dependencies:

```bash
pip install pytest coverage
coverage erase
coverage run --source=marathon_registration -m pytest -q CodeCoverageTest_marathon_registration.py
coverage report -m
```

The code coverage suite currently achieves **100% statement coverage**.

For branch coverage, run:

```bash
coverage erase
coverage run --branch --source=marathon_registration -m pytest -q BranchCoverageTest_marathon_registration.py
coverage report -m
```

The branch coverage suite currently achieves **100% branch coverage** (28 of 28 branches).

## Coverage evidence
The terminal-style report images are in `screenshots/`:
- `code_coverage.svg`
- `branch_coverage.svg`

Lab 7 work can be added to this repository separately.
