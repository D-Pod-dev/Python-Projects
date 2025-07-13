r"""
cd C:\Users\podno\Documents\Python-Projects\Algorithms-Exercises\Exercises\Section 1\Chapter 1\Exercise 3
python -m unittest test_exercise_1_1_3
"""
import unittest
from exercise_1_1_3 import list_searcher

class TestFindFunction(unittest.TestCase):

    def test_find_existing_element_returns_index(self):
        self.assertEqual(list_searcher([1,4,6,3], 4), 1)
    
    def test_find_nonexisting_element_returns_None(self):
        self.assertEqual(list_searcher([1,4,6,3], 2), None)
    
    def test_0_element_array_returns_None(self):
        self.assertEqual(list_searcher([], 0), None)

    def test_multiple_occurences_returns_first_occurence(self):
        self.assertEqual(list_searcher([1, 30, 4, 48, 4], 4), 2)
    
    def test_1_element_array(self):
        self.assertEqual(list_searcher([1], 1), 0)
    
    def test_find_first_element(self):
        self.assertEqual(list_searcher([2, 0, 4, 6, 3, 5, 8], 2), 0)
    
    def test_find_last_element(self):
        self.assertEqual(list_searcher([2, 0, 4, 6, 3, 5, 8], 8), 6)
    
if __name__ == "__main__":
    unittest.main()