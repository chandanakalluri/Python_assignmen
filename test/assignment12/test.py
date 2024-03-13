import unittest
from Python_assignmen.src.assignment12.util import min_along_axis_1, max_of_min, matrix


class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=3
        min_values = min_along_axis_1(matrix)
        res1=max_of_min(min_values)
        self.assertEqual(res1, res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
