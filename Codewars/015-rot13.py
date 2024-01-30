# Links https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''

def rot13(message):
    _  = 'abcdefghijklm'
    __ = 'nopqrstuvwxyz'
    a = []
    for i in message:
        if i.islower() and i in _:
         a.append(__[_.index(i)])
        elif i.isupper() and i.lower() in _:
         a.append(__[_.index(i.lower())].upper())
        elif i.isupper() and i.lower() in __:
         a.append(_[__.index(i.lower())].upper())
        elif i.islower() and i in __:
         a.append(_[__.index(i)])
        else:
          a.append(i)
    return ''.join(a)

print(rot13('annnn1n aaaaa'))