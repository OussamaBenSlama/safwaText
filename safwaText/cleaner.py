import re

def remove_tashkeel(text):
    """
    Remove Arabic diacritics (Tashkeel) from text.
    
    Args:
        text (str): Input Arabic text.
    
    Returns:
        str: Text without diacritics.
    """
    arabic_diacritics = re.compile(r'[\u0617-\u061A\u064B-\u0652]')
    return re.sub(arabic_diacritics, '', text)

def normalize_text(text):
    """
    Normalize Arabic text by standardizing characters.
    
    Args:
        text (str): Input Arabic text.
    
    Returns:
        str: Normalized text.
    """
    text = re.sub(r'[إأآا]', 'ا', text)  
    text = re.sub(r'ؤ', 'و', text)      
    text = re.sub(r'ئ', 'ي', text)      
    text = re.sub(r'ة', 'ه', text)      
    text = re.sub(r'ى', 'ي', text)      
    text = re.sub(r'ـ', '', text)      
    return text

def remove_non_arabic(text):
    """
    Remove non-Arabic characters from text.
    
    Args:
        text (str): Input text.
    
    Returns:
        str: Text with only Arabic characters and whitespace.
    """
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)  
    return text