def hey(phrase):
    phrase = phrase.strip()
    if not phrase:
        # If a phrase is empty
        return 'Fine. Be that way!'
    if phrase.isupper():
        # Is it shouting?
        return 'Whoa, chill out!'
    if phrase[-1] == '?':
        return 'Sure.'
    # In any other case
    return 'Whatever.'
