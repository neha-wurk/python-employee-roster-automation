
import unittest
from datetime import date
from main import generate_roster


class TestRoster(unittest.TestCase):

    def setUp(self):
        self.roster = generate_roster(date(2026, 11, 1))

    def test_seven_days_generated(self):
        self.assertEqual(len(self.roster), 35)

    def test_five_assignments_per_day(self):
        for day in range(7):
            daily = self.roster[day * 5:(day + 1) * 5]
            self.assertEqual(len(daily), 5)

    def test_no_duplicate_employee_per_day(self):
        for day in range(7):
            daily = self.roster[day * 5:(day + 1) * 5]
            employees = [item["Employee"] for item in daily]
            self.assertEqual(len(employees), len(set(employees)))

    def test_shift_rotation(self):
        day_one = [
            item["Employee"] for item in self.roster[:5]
        ]
        day_two = [
            item["Employee"] for item in self.roster[5:10]
        ]

        self.assertNotEqual(day_one, day_two)


if __name__ == "__main__":
    unittest.main()
  
