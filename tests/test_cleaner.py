import sys
import os
import unittest
from safwaText.cleaner import remove_tashkeel, normalize_text, remove_non_arabic

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
class TestCleaner(unittest.TestCase):
    def test_remove_tashkeel(self):
        self.assertEqual(remove_tashkeel("مُحَمَّد"), "محمد")
        self.assertEqual(remove_tashkeel("قُرْآن"), "قرآن")

    def test_normalize_text(self):
        self.assertEqual(normalize_text("أَحْمَد"), "احمد")
        self.assertEqual(normalize_text("إسلام"), "اسلام")
        self.assertEqual(normalize_text("مَدْرَسَة"), "مدرسه")

    def test_remove_non_arabic(self):
        self.assertEqual(remove_non_arabic("Hello مرحبا 123!"), "مرحبا")
        self.assertEqual(remove_non_arabic("Python programming لغة برمجة"), "لغة برمجة")



if __name__ == "__main__":
    unittest.main()