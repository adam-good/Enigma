

class Plugboard(object):

    dictionary = dict()
    alphabet = ''

    def __init__(self, alphabet, subst_list):
        self.alphabet = alphabet
    
    def set_plugboard(self, subst_list):
       for pair in subst_list:
            val1 = pair[0]
            val2 = pair[1]

            self.dictionary[val1] = val2
            self.dictionary[val2] = val1

    def encipher(self, input_char):
        if not input_char in self.dictionary:
            return input_char
        else:
            return self.dictionary[input_char]
    