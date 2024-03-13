import unittest

from Python_assignmen.src.assignment10.util import manipulate_array
class MyTestCase(unittest.TestCase):
    def test_something(self):
        input_str = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"

        # Call the function
        floor_arr, inc_arr, filtered_arr = manipulate_array(input_str)

        self.assertEqual(manipulate_array(input_str), ([1, 2, 3, 4, 5, 6, 7, 8, 9],
 [2.1, 3.2, 4.3, 5.4, 6.5, 7.6, 8.7, 9.8, 10.9],
 [1.1, 2.2, 3.3, 4.4, 5.5, 7.7, 8.8, 9.9]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
