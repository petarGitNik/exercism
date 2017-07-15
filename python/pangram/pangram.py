def is_pangram(phrase):
    phrase = list(filter(lambda char: char.isalpha(), phrase.lower()))
    return len(set(phrase)) == 26
