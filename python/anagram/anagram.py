from collections import defaultdict

def detect_anagrams(word, candidates):
    matches = []
    w = word_to_dict(word.lower())
    for candidate in candidates:
        if w == word_to_dict(candidate.lower()) and word.lower() != candidate.lower():
            matches.append(candidate)
    return matches

def word_to_dict(word):
    d = defaultdict(int)
    for letter in word:
        d[letter] += 1
    return d
