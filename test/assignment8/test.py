import unittest

from Python_assignmen.src.assignment8.util import avg
class MyTestCase(unittest.TestCase):
    def test_something(self):
        res=avg()
        self.assertEqual(res,   '78.00')







if __name__ == '__main__':
    unittest.main()
