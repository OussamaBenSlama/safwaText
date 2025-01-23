# SafwaText

**SafwaText** is a Python package for cleaning, normalizing, and stemming Arabic text effortlessly. Whether you're working on NLP projects or need to preprocess Arabic text, SafwaText simplifies the process.

## Features

- **Remove Tashkeel (diacritics):** Simplifies text by removing diacritical marks.
- **Normalize Arabic text:** Converts text into a consistent format (e.g., unifying forms of "أ", "إ", and "ا").
- **Filter Non-Arabic Characters:** Removes any characters not part of the Arabic script.


## Installation

Install the package directly from PyPI using pip:
    ```bash
    pip install safwaText

## Usage
    ```bash
    from safwa_text import remove_tashkeel, normalize_text, remove_non_arabic

    text = "مُحَمَّدٌ"
    cleaned_text = remove_tashkeel(text)
    print(cleaned_text)  # Output: "محمد"

    normalized_text = normalize_text("أحمد")
    print(normalized_text)  # Output: "احمد"

    arabic_only_text = remove_non_arabic("هذا نص 123 مع رموز !@#")
    print(arabic_only_text)  # Output: "هذا نص  مع رموز "
    ```
## Contributing
We welcome contributions to SafwaText!
- Report Issues: Found a bug? Open an issue in the GitHub repository.
- Submit Pull Requests: Have improvements or new features? Feel free to contribute!


## License
SafwaText is licensed under the Apache-2.0 license.