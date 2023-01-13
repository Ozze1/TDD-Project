import sys
import unittest

def fuel_required(mass):
    fuel = mass // 3-2
    if fuel <= 0:
        return 0
    return fuel + fuel_required(fuel)


def total_fuel_required(input__):
    with open('input_day_01_part_01_02') as f:
        masses = [int(line.strip()) for line in f]
    return sum(fuel_required(mass) for mass in masses)


class TestFuelRequired(unittest.TestCase):
    def test_fuel_required(self):
        self.assertEqual(fuel_required(14), 2)
        self.assertEqual(fuel_required(1969),  966)
        self.assertEqual(fuel_required(100756), 50346)


    def  test_total_fuel_required(self):
        self.assertEqual(total_fuel_required(''), 51316)


if __name__ == "__main__":
    input__ = sys.argv[1]
    result = total_fuel_required('')
    print(result)
