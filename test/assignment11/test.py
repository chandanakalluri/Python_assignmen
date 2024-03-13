import unittest

from Python_assignmen.src.assignment11.util import min_max
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=min_max()
        self.assertEqual(res, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
