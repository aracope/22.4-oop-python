"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Finds random words from a file.

    >>> wf = WordFinder("three_words.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "axolotl"]
    True

    >>> wf.random() in ["cat", "dog", "axolotl"]
    True

    >>> wf.random() in ["cat", "dog", "axolotl"]
    True

    # Test empty file
    >>> empty_wf = WordFinder("only_blank_lines.txt")  # Assume only_blank_lines.txt is an empty file
    0 words read

    >>> empty_wf.words  # Should be an empty list
    []

    # Test reproducible random results using random.seed()
    >>> random.seed(1)  # Set a seed for consistent output
    >>> wf.random() in ["cat", "dog", "axolotl"]
    True

    >>> random.seed(2)
    >>> wf.random() in ["cat", "dog", "axolotl"]
    True
    """

    def __init__(self, file_path):
        """Reads words from file and stores them in a list."""
        with open(file_path, "r") as file:
            # Remove empty lines
            self.words = [line.strip() for line in file if line.strip()]
        # Print count of words read
        print(f"{len(self.words)} words read")

    def random(self):
        """Returns a random word from the list."""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """A special wordfinder that excludes blank lines and comments

    >>> swf = SpecialWordFinder("test_mixed.txt")
    3 words read

    >>> swf.words  # Should only contain valid words
    ['apple', 'banana', 'carrot']

    >>> swf.random() in ['apple', 'banana', 'carrot']
    True

    # Test file with blank lines only
    >>> swf_blank = SpecialWordFinder("only_blank_lines.txt")
    0 words read

    >>> swf_blank.words
    []

    # Test reproducible results
    >>> random.seed(1)
    >>> swf.random() in ['apple', 'banana', 'carrot']
    True

    >>> random.seed(2)
    >>> swf.random() in ['apple', 'banana', 'carrot']
    True
    """

    def __init__(self, file_path):
        """Reads words from file and stores them in a list."""
        with open(file_path, "r") as file:
            # Remove empty lines
            self.words = [
                line.strip()
                for line in file
                if line.strip() and not line.startswith("#")
            ]
        # Print count of words read
        print(f"{len(self.words)} words read")
