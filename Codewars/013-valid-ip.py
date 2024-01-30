# Links https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

'''
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
Valid inputs examples:

Examples of valid inputs:
1.2.3.4
123.45.67.89

Invalid input examples:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Notes:

    Leading zeros (e.g. 01.02.03.04) are considered invalid
    Inputs are guaranteed to be a single string


'''

def is_valid_IP(strng):
    strng = strng.split('.')
    if len(strng) == 4:
        for x in strng:
            if not x.isdigit() or int(x) > 255 or x != str(int(x)):
                return False
        return True
    else:
        return False
    
# Best Practice
    # def is_valid_IP(s):
    # return s.count('.')==3 and all(o.isdigit() and 0<=int(o)<=255 and str(int(o))==o for o in s.split('.'))
    

print(is_valid_IP('12.255.56.1'))