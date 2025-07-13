r"""
cd C:\Users\podno\Documents\Python-Projects\Algorithms-Exercises\Exercises\Section 1\Chapter 1\Exercise 2
python -m unittest test_exercise_1_1_2
"""
import unittest
from exercise_1_1_2 import nonincreasing_insertion_sort

class TestSortFunction(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(nonincreasing_insertion_sort([4, 3, 5, 1, 2]), [5, 4, 3, 2, 1])
    
    def test_sort_1_element_array(self):
        self.assertEqual(nonincreasing_insertion_sort([1]), [1])
    
    def test_sort_repeating_number_array(self):
        self.assertEqual(nonincreasing_insertion_sort([4, 4, 4, 4, 4, 4, 4]), [4, 4, 4, 4, 4, 4, 4])