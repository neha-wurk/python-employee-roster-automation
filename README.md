
# Python Employee Roster Automation

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/neha-wurk/python-employee-roster-automation/actions/workflows/python-tests.yml/badge.svg)

## Project Overview

A Python-based employee roster automation application designed to generate weekly employee shift schedules, rotate assignments and export roster data into CSV format.

This project demonstrates practical Python programming, automation logic, data handling and automated software testing.

## Features

- Automated weekly employee roster generation.
- Morning, evening and night shift allocation.
- Daily employee shift rotation.
- Duplicate employee assignment validation.
- CSV export of generated rosters.
- Automated unit testing.
- Continuous Integration using GitHub Actions.

## Technologies Used

- Python 3.11
- CSV module
- Python unittest
- GitHub
- GitHub Actions

## Project Structure

```text
python-employee-roster-automation/
├── main.py
├── test_roster.py
├── README.md
├── LICENSE
├── .gitignore
└── .github/
    └── workflows/
        └── python-tests.yml
```

## How to Run

Clone the repository:

```bash
git clone https://github.com/neha-wurk/python-employee-roster-automation.git
```

Run the application:

```bash
python main.py
```

The application generates a seven-day roster and exports it to `employee_roster.csv`.

## Running Automated Tests

```bash
python -m unittest -v
```

## Continuous Integration

GitHub Actions automatically runs the test suite when code is pushed to the main branch or a pull request targets main.

## Future Enhancements

- Employee leave management.
- Public holiday scheduling.
- Weekend allocation and fairness.
- Minimum rest-period validation.
- Excel report generation.
- Configurable employee and shift requirements.

## Author

GitHub: [@neha-wurk](https://github.com/neha-wurk)

## License

MIT License.
