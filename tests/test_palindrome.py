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

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("Carlos"))
        self.assertFalse(is_palindrome("Etec"))
        self.assertFalse(is_palindrome("Catolico"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome("b"))
        self.assertTrue(is_palindrome("C?"))

if __name__ == '__main__':
    unittest.main()