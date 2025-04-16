import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("Ana"))
        self.assertTrue(is_palindrome("Álula"))
        self.assertTrue(is_palindrome("Oto"))

if __name__ == '__main__':
    unittest.main()