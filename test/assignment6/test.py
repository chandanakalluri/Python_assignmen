import unittest
from Python_assignmen.src.assignment6.util import patt_l

class MyTestCase(unittest.TestCase):
    def test_something(self):
      expected_result = [
            '  H  ',
            ' HHH ',
            'HHHHH',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHHHHHHHHHHHHHH  ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            ' HHH         HHH        ',
            '            HHHHH ',
            '             HHH  ',
            '              H   ',
        ]
      self.assertEqual(expected_result, patt_l(3))  # add assertion here

if __name__ == '__main__':
    unittest.main()