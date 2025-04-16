import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("Ana"))
        self.assertTrue(is_palindrome("Álula"))
        self.assertTrue(is_palindrome("Oto"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("Somos o no somos"))
        self.assertTrue(is_palindrome("Sé verlas al revés"))
        self.assertTrue(is_palindrome("Anita lava la tina"))

if __name__ == '__main__':
    unittest.main()