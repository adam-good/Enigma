import string
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

ALPHABET = string.ascii_uppercase
PLUGBOARD_LIST = [('A', 'B'), ('D', 'Z'), ('F', 'O')]

class Enigma(object):
    '''Object to handle Enigma encryption. Based on Enigma Machine'''
    def __init__(self, offset1, offset2, offset3):
        self.rot1 = Rotor(offset1, rotor_num=1)
        self.rot2 = Rotor(offset2, rotor_num=2)
        self.rot3 = Rotor(offset3, rotor_num=3)
        self.reflector = Reflector(ALPHABET)
        self.plugboard = Plugboard(ALPHABET, PLUGBOARD_LIST)

    #TODO: Do this better
    def set_rotors(self, offset1, offset2, offset3):
        '''Set the values of the rotors'''
        self.rot1.offset = offset1
        self.rot2.offset = offset2
        self.rot3.offset = offset3

    #TODO: Implement this correctly
    def increment_rotors(self):
        '''Increment the rotors according to the Enigma algorithm'''
        self.rot1.increment()
        if self.rot1.offset == 3:
            self.rot2.increment()
            if self.rot2.offset == 2:
                self.rot3.increment()

    def encipher(self, msg):
        '''Encipher the message according to the Enigma algorithm'''
        output = ''
        for val in msg:
            val = self.plugboard.encipher(val)

            self.increment_rotors()
            val = self.rot1.encipher(val)
            val = self.rot2.encipher(val)
            val = self.rot3.encipher(val)

            val = self.reflector.encipher(val)

            val = self.rot3.decipher(val)
            val = self.rot2.decipher(val)
            val = self.rot1.decipher(val)

            val = self.plugboard.encipher(val)

            output = output + val
        return output

