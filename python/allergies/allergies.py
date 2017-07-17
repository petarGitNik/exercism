class Allergies(object):
    # lst = []

    ALLERGIES = {
        'eggs' : 1
        'peanuts' : 2
        'shellfish' : 4
        'strawberries' : 8
        'tomatoes' : 16
        'chocolate' : 32
        'pollen' : 64
        'cats' : 128
    }

    def __init__(self, score):
        self.score = score

    def is_alergic_to(self, alergy):
        pass
