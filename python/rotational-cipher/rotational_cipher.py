def rotate(plaintext, rot):
    cipertext = []

    # ASCII table:
    # https://en.wikipedia.org/wiki/ASCII#Printable_characters
    # -97 for lower, -65 for upper

    for char in plaintext:
        if not char.isalpha():
            cipertext.append(char)
        elif char.isupper():
            letter = (ord(char) - 65 + rot) % 26
            if letter > 26:
                letter -= 26
            letter += 65
            cipertext.append(chr(letter))
        else:
            letter = (ord(char) - 97 + rot) % 26
            if letter > 26:
                letter -= 26
            letter += 97
            cipertext.append(chr(letter))

    return ''.join(cipertext)
