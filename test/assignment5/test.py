import unittest

from python_assignments.src.assignment5.util import print_formatted
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=print_formatted(2)
        self.assertEqual(" 1  1  1  1\n 2  2  2 10", res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
