class Allergies(object):

    ALLERGIES = {
        'eggs' : 1,
        'peanuts' : 2,
        'shellfish' : 4,
        'strawberries' : 8,
        'tomatoes' : 16,
        'chocolate' : 32,
        'pollen' : 64,
        'cats' : 128,
    }

    def __init__(self, score):
        self.lst = [allergy for allergy, grade in self.ALLERGIES.items() if score & grade]

    def is_allergic_to(self, allergy):
        return allergy in self.lst
