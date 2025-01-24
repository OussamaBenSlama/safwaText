from .cleaner import remove_tashkeel, normalize_text

PREFIX_GROUPS = (
    ('فلىست', 'الاست', 'افاست'),          
    ('اتست','اىست','فاست','ءاست','انهم','ءانى','والم','باست','كمست','والا'),     
    ('مست','ولت','فلى','فلن','فلل','فهو','فهم','فال','ىست','تست','است','فهى','سيا','فلا','ءست','بمس','لىت'),               
    ('اى','ال','ون','فى','فب','فت','لي','فن','وب','فا','ول','وو','اف','لا','ات','وى','وت','اا','ال','ست','سى','يس','يت','گت','ىى','تت','سي'),                  
    ('ا','ل','ب','و','ف','ى','ت','ي')                      
)

SUFFIX_GROUPS = (
    ('كموها', 'ناهما', 'ناكمو'),         
    ('موهم', 'موهن', 'ناكم','يكما','موهم','موهن','ناگم','نوهن','ونهم','ناهم','ونگم','توهم','اتها','اتهم','يانه','اءهم'),            
    ('تنا','نها','تان','ناك','ونه','كما','ناه','هما','وعا','نهم','وهم','ونى','وعن','تها','تهم','نكم','هات','هان','تان','تهن','وكم','ونه','ونك','انك'),                
    ('وا', 'ون', 'هن','هم','هو','هي','هى','ها','ان','وك','اك','اه','كن','ات','كم'),                   
    ('ت', 'ك', 'ى','ه','ا','ي')                     
)


ARTICLES = {'بال', 'فال', 'ال', 'ولل', 'كال', 'ل'}

def remove_arabic_articles(word: str) -> str:
    """Remove definite articles and common prefixes from Arabic words."""
    for article in sorted(ARTICLES, key=len, reverse=True):
        if word.startswith(article) and len(word) > len(article) + 2:
            return word[len(article):]
    return word

def remove_arabic_prefixes(word: str) -> str:
    """Remove Arabic prefixes from a word.
    
    Args:
        word: Input Arabic word
        
    Returns:
        Word with prefixes removed
    """
    for group in PREFIX_GROUPS:
        for prefix in group:
            if word.startswith(prefix) and len(word) > len(prefix) + 2:
                return word[len(prefix):]
    return word

def remove_arabic_suffixes(word: str) -> str:
    """Remove Arabic suffixes from a word.
    
    Args:
        word: Input Arabic word
        
    Returns:
        Word with suffixes removed
    """
    for group in SUFFIX_GROUPS:
        for suffix in group:
            if word.endswith(suffix) and len(word) > len(suffix) + 2:
                return word[:-len(suffix)]
    return word

def stem_word(word: str) -> str:
    """Apply full stemming process to a single Arabic word.
    
    Args:
        word: Input Arabic word
        
    Returns:
        Stemmed Arabic word
    """
    processed = remove_tashkeel(word)
    processed = normalize_text(processed)
    processed = remove_arabic_articles(processed)
    processed = remove_arabic_suffixes(processed)
    processed = remove_arabic_prefixes(processed)
    return processed

def arabic_stemmer(text: str) -> str:
    """Process text through complete Arabic stemming pipeline.
    
    Args:
        text: Input Arabic text
        
    Returns:
        Stemmed Arabic text
    """
    return ' '.join(stem_word(word) for word in text.split())