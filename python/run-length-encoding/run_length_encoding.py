import re
from collections import deque

def decode(phrase):
    decoded = []
    #index = 1
    #phrase = re.findall(r'\s|\d+|\D+', phrase)
    phrase = re.findall(r'\s|\d+|\D', phrase)
    phrase = list(map(lambda x: int(x) if x.isnumeric() else x, phrase))
    phrase = deque(phrase)
    while len(phrase) > 0:
        element = phrase.popleft()
        if len(phrase) == 0:
            decoded.append(element)
            break
        #if is_multipliable(element, phrase[0]):
        if is_numeric(element):
            decoded.append(element *  phrase.popleft())
            #index += 2
        else:
            decoded.append(element)
            #index += 1
    return ''.join(decoded)

def is_numeric(num):
    try:
        num.isnumeric()
    except:
        return True
    return False

def is_multipliable(p, q):
    try:
        m = p * q
    except:
        return False
    return True

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
