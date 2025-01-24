import sys
import os
import unittest
from safwaText.stopwords import remove_stopwords

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



class TestStopwords(unittest.TestCase):
    def test_remove_stopwords(self):
        self.assertEqual(remove_stopwords("كتاب على الطاولة"), ("كتاب الطاولة"))
        self.assertEqual(remove_stopwords("هذا كتاب جديد"), ("كتاب جديد"))
        

if __name__ == "__main__":
    unittest.main()