from random import choice

class SubstitutionCipher(object):
    '''Substitution Cipher'''
    alphabet = ''
    substituion = ''

    def __init__(self, alphabet):
        if len(alphabet) % 2 != 0:
            raise ValueError('rotor alphabet of odd length')
        self.alphabet = alphabet
        self.generate_substitution_key()

    def generate_substitution_key(self):
        '''populates self.substitution based on self.alphabet'''
        self.substituion = ''
        tmp = list(self.alphabet)

        for key in self.alphabet:
            val = key
            while val == key:
                val = choice(tmp)
            self.substituion = self.substituion + val
            tmp.remove(val)

    def encipher(self, input_char):
        '''Return the character mapped to the input character'''
        if input_char in self.alphabet:
            index = self.alphabet.index(input_char)
            return self.substituion[index]
        else:
            return input_char

    def decipher(self, input_char):
        '''TODO'''
        if input_char in self.substituion:
            index = self.substituion.index(input_char)
            return self.alphabet[index]
        else:
            return input_char
        