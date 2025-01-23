import unittest
from safwaText.cleaner import remove_tashkeel, normalize_text, remove_non_arabic

class TestCleaner(unittest.TestCase):
    def test_remove_tashkeel(self):
        self.assertEqual(remove_tashkeel("مُحَمَّدٌ"), "محمد")
        self.assertEqual(remove_tashkeel("كِتَابٌ"), "كتاب")

    def test_normalize_text(self):
        self.assertEqual(normalize_text("أحمد"), "احمد")
        self.assertEqual(normalize_text("مسؤول"), "مسوول")
        self.assertEqual(normalize_text("سئل"), "سيل")
        self.assertEqual(normalize_text("جامعة"), "جامعه")
        self.assertEqual(normalize_text("مشى"), "مشي")
        self.assertEqual(normalize_text("كــــلمة"), "كلمة")

    def test_remove_non_arabic(self):
        self.assertEqual(remove_non_arabic("هذا نص 123 مع رموز !@#"), "هذا نص  مع رموز ")
        self.assertEqual(remove_non_arabic("Hello العالم"), " العالم")

if __name__ == "__main__":
    unittest.main()