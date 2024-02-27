import unittest
from P1 import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindromo_not_spaces(self):
        self.assertTrue(is_palindrome("Otto"))
        self.assertTrue(is_palindrome("sometemos"))
        self.assertTrue(is_palindrome("reconocer"))
        
    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome("Oso baboso"))
        self.assertTrue(is_palindrome("Somos o no somos"))
        self.assertTrue(is_palindrome("Yo soy"))
        
    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("casa"))
        self.assertFalse(is_palindrome("mesa"))
        self.assertFalse(is_palindrome("perro"))

if __name__ == "__main__":
    unittest.main()