from crypto.substitution_cipher import SubstitutionCipher
# from random import choice

SUBST = "BAWXYZSTUVOPQRKLMNGHIJCDEF"

class Reflector(SubstitutionCipher):

    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.substituion = SUBST
#        self.generate_substitution_key()
    
    def generate_substitution_key(self):
        """Populates self.substitution based on self.alphabet"""
        self.substituion = [None] * len(self.alphabet)
        tmp = list(self.alphabet)

        for key in self.alphabet:
            if key in self.substituion:
                continue
            
            tmp.remove(key)
            val = choice(tmp)
            tmp.remove(val)

            index = self.alphabet.index(key)
            self.substituion[index] = val

            index = self.alphabet.index(val)
            self.substituion[index] = key







                        