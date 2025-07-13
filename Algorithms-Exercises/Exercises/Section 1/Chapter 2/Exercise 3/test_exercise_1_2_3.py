r"""
cd C:\Users\podno\Documents\Python-Projects\Algorithms-Exercises\Exercises\Section 1\Chapter 2\Exercise 3
python -m unittest test_exercise_1_2_3
"""
import unittest
from exercise_1_2_3 import rep_occurences_searcher

class TestBinaryAddition(unittest.TestCase):
    
    def test_one_occurence(self):
        self.assertEqual(rep_occurences_searcher([1, 5, 2, 67, 3, 95, 24, 55], 24), False)
    
    def test_two_occurences(self):
        self.assertEqual(rep_occurences_searcher([90, 78, 8, 34, 90, 5], 90), True)
    
    def test_no_occurences(self):
        self.assertEqual(rep_occurences_searcher([8, 67, 39, 4, 76], 5), False)
    
    def test_empty_list(self):
        self.assertEqual(rep_occurences_searcher([], 9), False)
    
    def test_1_item_list(self):
        self.assertEqual(rep_occurences_searcher([4], 4), False)
    
    def test_1st_and_last_occurence(self):
        self.assertEqual(rep_occurences_searcher([9, 4, 6, 13, 45, 6, 9], 9), True)
