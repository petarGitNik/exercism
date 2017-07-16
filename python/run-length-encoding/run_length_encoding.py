import re
from collections import deque

def decode(phrase):
    """
    A horrible solution! Any suggestion if welcome. Here is how it goes: split
    numbers from other non-numeric characters, cast numeric strings into integers,
    and transform the list into deque (so I could use popleft() method). In each
    iteration I pop the left element and test if it's a number. If it's not, append
    it, else multiply it with the next popped element.
    """
    decoded = []
    phrase = re.findall(r'\s|\d+|\D', phrase)
    phrase = list(map(lambda x: int(x) if x.isnumeric() else x, phrase))
    phrase = deque(phrase)
    while len(phrase) > 0:
        element = phrase.popleft()
        if len(phrase) == 0:
            decoded.append(element)
            break
        if is_numeric(element):
            decoded.append(element *  phrase.popleft())
        else:
            decoded.append(element)
    return ''.join(decoded)

def is_numeric(num):
    """
    If the input is an integer, then isnumeric() test will fail. Therefore, it
    is integer. It's very unfortunate function. This because isnumeric() only
    works for string objects.
    """
    try:
        num.isnumeric()
    except:
        return True
    return False

def encode(phrase):
    coded = []
    count_buffer = 1

    if phrase == '':
        return ''

    for index in range(1, len(phrase)):
        if phrase[index] == phrase[index - 1]:
            count_buffer += 1
        else:
            if count_buffer != 1: coded.append(count_buffer)
            coded.append(phrase[index - 1])
            count_buffer = 1
    else:
        if count_buffer != 1: coded.append(count_buffer)
        coded.append(phrase[index])

    return ''.join([str(char) for char in coded])
