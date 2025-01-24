from .cleaner import remove_tashkeel, normalize_text, remove_non_arabic
from .stopwords import remove_stopwords
from .stemmer import stem_word, remove_arabic_prefixes , remove_arabic_suffixes ,arabic_stemmer,remove_arabic_articles

__all__ = ["remove_tashkeel", "normalize_text", "remove_non_arabic","remove_arabic_articles",
           "remove_stopwords","stem_word", "remove_arabic_prefixes","remove_arabic_suffixes","arabic_stemmer"]