from enigma.enigma import Enigma
from enigma.enigma import Rotor
import sys


e = Enigma(0,0,0)

rotorNums = []
rotorOffsets = []
rotors = []

print("[*] Which Rotors Would You Like To Use? (1-8)")
for i in range(1, 4):
    num = int(raw_input("Position " + str(i) + ") "))
    
    while num < 1 or num > 8:
        num = int(raw_input("Invalid Input! Try again: "))

    rotorNums.append(num)

print('')

print("[*] Set Starting Positions For Each Rotor: (0-25)")
for i in range(1, 4):
    num = int(raw_input("Rotor Position " + str(i) + ") "))

    while num < 0 or num > 25:
        num = int(raw_input("Invalid Input! Try again: "))

    rotorOffsets.append(num)

     
for i in range(3):
    offset = rotorOffsets[i]
    num = rotorNums[i]
    rotor = Rotor(offset, num)
    rotors.append(rotor)

e.rot1 = rotors[0]
e.rot2 = rotors[1]
e.rot3 = rotors[2]



msg = raw_input("Enter The Secret Message: ").upper()
print("You Entered: " + msg)
msg = e.encipher(msg)
print("Cipher Text: " + msg)