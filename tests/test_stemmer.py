import sys
import os
import unittest
from safwaText.stemmer import remove_arabic_prefixes, remove_arabic_suffixes, arabic_stemmer, remove_arabic_articles

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestStemmer(unittest.TestCase):
    def test_remove_arabic_articles(self):
        self.assertEqual(remove_arabic_articles("بالكتاب"), "كتاب")
        self.assertEqual(remove_arabic_articles("مدرسة"), "مدرسة")

    def test_remove_arabic_prefixes(self):
        self.assertEqual(remove_arabic_prefixes("استخدام"), "خدام")
        self.assertEqual(remove_arabic_prefixes("مدرسة"), "مدرسة")

    def test_remove_arabic_suffixes(self):
        self.assertEqual(remove_arabic_suffixes("كتابهم"), "كتاب")
        self.assertEqual(remove_arabic_suffixes("مدرسة"), "مدرسة")

    def test_arabic_stemmer(self):
        self.assertEqual(arabic_stemmer("كتابهم"), "كتاب")
        self.assertEqual(arabic_stemmer("بالمدارس"), "مدارس")
        

if __name__ == "__main__":
    unittest.main()
