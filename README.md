# SafwaText

**SafwaText** is a Python package for cleaning, normalizing, and stemming Arabic text effortlessly. Whether you're working on NLP projects or need to preprocess Arabic text, SafwaText simplifies the process.

## Features
- **Remove Tashkeel (diacritics):** Simplifies text by removing diacritical marks.
- **Normalize Arabic text:** Converts text into a consistent format.
- **Filter Non-Arabic Characters:** Removes any characters not part of the Arabic script, including numbers, punctuation, and symbols.
- **Remove Arabic Articles:** Strips common Arabic definite articles.
- **Remove Arabic Prefixes:** Removes common prefixes from words.
- **Remove Arabic Suffixes:** Removes common suffixes from words.
- **Arabic Stemming:** Applies a light stemming pipeline to Arabic words, including normalization, prefix/suffix removal, and article stripping.
- **Remove Stopwords:** Filters out common Arabic stopwords

## Installation
Install the package directly from PyPI using pip:
    ```bash
    pip install safwaText

## Usage
    ```bash
    from safwaText.cleaner import remove_tashkeel, normalize_text, remove_non_arabic
    from safwaText.stemmer import arabic_stemmer
    from safwaText.stopwords import remove_stopwords

    # Clean and normalize text
    input = "يذهب مُحَمَّدٌ للمَدْرَسَةِ كل صباح"
    cleaned_text = remove_tashkeel(input) 
    normalized_text = normalize_text(cleaned_text) 
    filtered_text = remove_non_arabic(normalized_text) 

    # Apply light stemming
    stemmed_text = arabic_stemmer(filtered_text)  

    # Remove stopwords
    final_output = remove_stopwords(stemmed_text)

    print(final_output)  # Output: "ذهب محمد مدرس صباح"
    ```
    
## Contributing
Contributions are welcome! If you'd like to improve this extension:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
3. Commit your changes and push to your branch :
   ```bash
   git commit -m "Add feature: feature-name"
   git push origin feature-name
4. Open a pull request.

## License
SafwaText is licensed under the Apache-2.0 license.