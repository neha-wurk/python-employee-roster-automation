
from datetime import date, timedelta
import csv

EMPLOYEES = [
    "Ava",
    "Noah",
    "Mia",
    "Liam",
    "Sophia"
]

SHIFTS = {
    "Morning": 2,
    "Evening": 2,
    "Night": 1
}


def generate_roster(start_date, days=7):
    total_slots = sum(SHIFTS.values())

    if len(EMPLOYEES) < total_slots:
        raise ValueError("Not enough employees for all shifts.")

    roster = []

    for day in range(days):
        current_date = start_date + timedelta(days=day)
        assigned = set()

        for shift, required in SHIFTS.items():
            for position in range(required):
                employee_index = (
    day
    + sum(
        list(SHIFTS.values())[
            :list(SHIFTS.keys()).index(shift)
        ]
    )
    + position
) % len(EMPLOYEES)

                employee = EMPLOYEES[employee_index]

                if employee in assigned:
                    raise ValueError("Duplicate daily assignment.")

                assigned.add(employee)

                roster.append({
                    "Date": current_date.isoformat(),
                    "Day": current_date.strftime("%A"),
                    "Shift": shift,
                    "Employee": employee
                })

    return roster


def export_roster(roster, filename="employee_roster.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Date", "Day", "Shift", "Employee"]
        )
        writer.writeheader()
        writer.writerows(roster)


if __name__ == "__main__":
    roster = generate_roster(date.today())

    for entry in roster:
        print(entry)

    export_roster(roster)
    print("\nRoster exported successfully!")
