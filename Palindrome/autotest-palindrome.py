r"""
cd C:\Users\podno\Documents\Python-Projects
python -m unittest autotest-palindrome.py

"""
import unittest
from palindrome import palindrome

class TestBinaryAddition(unittest.TestCase):

    def test_non_palindrome(self):
        self.assertEqual(palindrome(2763), False)
    
    def test_palindrome(self):
        self.assertEqual(palindrome(26786762), True)
    
"""    def test_0(self):
        self.assertEqual(palindrome(), )
    
"""