import re

def is_isogram(word):
    """
    Check if the word/phrase has repeating letters. All non letter characters are
    removed. The set is a collection of non-repeating elements. If length of a word
    if different then the sum of its elements (letters), then the word/phrase is
    not an isogram.
    """
    word = re.sub(r'[^a-z]', '', word.lower())
    letters = set(word)
    return len(word) == len(letters)
