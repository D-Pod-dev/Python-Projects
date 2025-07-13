r"""
cd C:\Users\podno\Documents\Python-Projects\Algorithms-Exercises\Exercises\Section 1\Chapter 1\Exercise 4
python -m unittest test_exercise_1_1_4
"""
import unittest
from exercise_1_1_4 import binary_addition

class TestBinaryAddition(unittest.TestCase):

    def test_binary_add_two_1s(self):
        self.assertEqual(binary_addition([1], [1]), [1, 0])
    
    def test_binary_add_empty_arrays(self):
        self.assertEqual(binary_addition([], []), [0])
    
    def test_binary_add_different_length_arrays(self):
        self.assertEqual(binary_addition([1], [1, 0, 1]), [0, 1, 1, 0])
    
    def test_binary_add_two_0s(self):
        self.assertEqual(binary_addition([0], [0]), [0, 0])