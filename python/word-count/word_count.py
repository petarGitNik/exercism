import re

def word_count(phrase):
    phrase = re.sub(r'[^a-z0-9]', ' ', phrase.lower())
    count = {}
    for word in phrase.split():
        count[word] = count.get(word, 0) + 1
    return count
