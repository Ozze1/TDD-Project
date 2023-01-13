import unittest

def fuel_required (mass):
    return mass // 3 - 2

class TestFuelRequired (unittest.TestCase):
   def test_fuel_required(self):
    self.assertEqual(fuel_required(12), 2)
    self.assertEqual(fuel_required(14), 2)
    self.assertEqual(fuel_required(1969), 654)
    self.assertEqual(fuel_required(100756), 33583)

def main():

    with open('input_day_01_part_01_02') as f:
        masses = [int(line.strip()) for line in f]

    total_fuel = sum(fuel_required(mass) for mass in masses)
    print(total_fuel)

if __name__ == '__main__':
    main()
    unittest.main()
