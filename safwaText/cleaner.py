import re
from typing import List

# Pre-compile regex patterns for better performance
ARABIC_DIACRITICS = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
NORMALIZATION_MAPPING = {
    r'[إأآا]': 'ا',
    r'ؤ': 'و',
    r'ئ': 'ي',
    r'ة': 'ه',
    r'ى': 'ي',
    r'ـ': ''
}
ARABIC_CHARS_PATTERN = re.compile(r'[^\u0600-\u06FF\u0750-\u077F\s]')  
ARABIC_CLEAN_PATTERN = re.compile(
    r'[^\u0600-\u06FF\s]'    
    r'|[\u0660-\u0669]'      
    r'|[\u060C\u061B\u061F]' 
    r'|[\W_]'                
)
WHITESPACE_PATTERN = re.compile(r'\s+')

def remove_tashkeel(text: str) -> str:
    """Remove Arabic diacritics (Tashkeel) from text.
    
    Args:
        text: Input Arabic text with diacritics
        
    Returns:
        Cleaned text without diacritics
    """
    return ARABIC_DIACRITICS.sub('', text)

def normalize_text(text: str) -> str:
    """Standardize various Arabic character forms to their base equivalents.
    
    Handles:
    - Unified Alef forms
    - Ta' marbuta to ha
    - Ya variants
    - Tatweel removal
    
    Args:
        text: Input Arabic text
        
    Returns:
        Normalized Arabic text
    """
    text = remove_tashkeel(text)
    for pattern, replacement in NORMALIZATION_MAPPING.items():
        text = re.sub(pattern, replacement, text)
    return text





def remove_non_arabic(text: str) -> str:
    """Remove non-Arabic characters, numbers, punctuation, and symbols.
    
    Cleans text by:
    1. Removing all non-Arabic script characters
    2. Removing Arabic numerals (٠-٩)
    3. Removing punctuation/symbols (both Arabic and Western)
    4. Normalizing whitespace

    Args:
        text: Input text potentially containing mixed characters
        
    Returns:
        Cleaned Arabic text with only letters and single spaces
    """
    cleaned = ARABIC_CLEAN_PATTERN.sub(' ', text)
    return WHITESPACE_PATTERN.sub(' ', cleaned).strip()