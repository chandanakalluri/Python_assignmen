import unittest

from Python_assignmen.src.assignment13.driver import mean_var_std
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=mean_var_std()
        self.assertEqual(res, "[1.5 3.5]\n[1. 1.]\n1.11803398875")  # add assertion here


if __name__ == '__main__':
    unittest.main()
