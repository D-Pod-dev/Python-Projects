r"""
cd C:\Users\podno\Documents\Python-Projects\Algorithms-Exercises\Exercises\Section 1\Chapter 3\Exercise 2
python -m unittest test_exercise_1_3_2

"""
import unittest
from exercise_1_3_2 import merge

class TestBinaryAddition(unittest.TestCase):
    
    def test_merge_full_array(self):
        self.assertEqual(merge([0,2,4,1,3], 0, 2, 4), [0,1,2,3,4])
    
    def test_merge_part_of_array(self):
        self.assertEqual(merge([2,4,1,3,6,2,4,5,7,2], 2, 4, 7), [2,4,1,2,3,4,5,6,7,2])
    
    def test_merge_array_with_all_identical_numbers(self):
        self.assertEqual(merge([6,6,6,6,6], 0, 2, 4), [6,6,6,6,6])
    
    def test_one_item_list(self):
        self.assertEqual(merge([1], 0, 0, 0), [1])
    
    def test_empty_list(self):
        self.assertEqual(merge([], 0, 0, 0), [])
    
    def test_2_item_list(self):
        self.assertEqual(merge([3,2], 0, 0, 1), [2,3])
    
    def test_edge_case_beginning(self):
        self.assertEqual(merge([1,4,3,8,2,4,5], 0, 1, 3), [1,3,4,8,2,4,5])
    
    def test_edge_case_end(self):
        self.assertEqual(merge([0,2,5,6,10,4,5], 3, 4, 6), [0,2,5,4,5,6,10])
    
