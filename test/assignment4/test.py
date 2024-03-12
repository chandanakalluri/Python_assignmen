import unittest

from python_assignments.src.assignment4.util import merge_the_tools


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string, k = "ssdssfdde", 3
        res=merge_the_tools(string, k)
        self.assertEqual(res, merge_the_tools(string, k))  # add assertion here


if __name__ == '__main__':
    unittest.main()
