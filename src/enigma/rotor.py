from crypto.substitution_cipher import SubstitutionCipher

class Rotor(SubstitutionCipher):
    offset = 0

    def __init__(self, offset, rotor_num=None, alphabet=None):
        self.offset = offset
        if rotor_num != None:
            self.alphabet = ROTOR_ALPHABET
            self.substituion = ROTOR_WIRINGS[rotor_num]
        else:
            super(Rotor, self).__init__(alphabet)

    def increment(self):
        self.offset = (self.offset + 1) % len(self.alphabet)

    def encipher(self, input_char):
        if input_char in self.alphabet:
            index = (self.alphabet.index(input_char) + self.offset) % len(self.alphabet)
            val = self.substituion[index]
            return val
        else:
            return input_char

    def decipher(self, input_char):
        if input_char in self.substituion:
            index = (self.substituion.index(input_char) - self.offset) % len(self.substituion)
            val = self.alphabet[index]
            return val
        else:
            return input_char

ROTOR_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ROTOR_WIRING_I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
ROTOR_WIRING_II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
ROTOR_WIRING_III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
ROTOR_WIRING_IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
ROTOR_WIRING_V = 'VZBRGITYUPSDNHLXAWMJQOFECK'
ROTOR_WIRING_VI = 'JPGVOUMFYQBENHZRDKASXLICTW'
ROTOR_WIRING_VII = 'NZJHGRCXMYSWBOUFAIVLPEKQDT'
ROTOR_WIRING_VIII = 'FKQHTLXOCBJSPDZRAMEWNIUYGV'

ROTOR_WIRINGS = {
    1 : ROTOR_WIRING_I,
    2 : ROTOR_WIRING_II,
    3 : ROTOR_WIRING_III,
    4 : ROTOR_WIRING_IV,
    5 : ROTOR_WIRING_V,
    6 : ROTOR_WIRING_VI,
    7 : ROTOR_WIRING_VII,
    8 : ROTOR_WIRING_VIII
}
