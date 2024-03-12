import unittest

from python_assignments.src.assignment7.util import find_day
class MyTestCase(unittest.TestCase):
    def test_something(self):
        month, day, year = map(int, input().split())
        res=find_day(month, day, year)
        self.assertEqual(res, 'TUESDAY')  # add assertion here


if __name__ == '__main__':
    unittest.main()
