import unittest
from Python_assignmen.src.assignment14.util import mean_var_std

class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=mean_var_std()
        self.assertEqual(res, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
