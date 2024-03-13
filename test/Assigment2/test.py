import unittest
from Python_assignmen.src.assignment2.util import second_la
class MyTestCase(unittest.TestCase):
    def test_second_la(self):
        res = second_la()
        self.assertEqual(res, 44)
if __name__ == '__main__':
    unittest.main()
