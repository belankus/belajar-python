# Links : https://www.codewars.com/kata/55908aad6620c066bc00002a

'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

# def xo(s):
#     o, x = ['','']
#     for h in s:
#         if h.lower() == 'o':
#             o += h.lower()
#         elif h.lower() == 'x':
#             x += h.lower()
        
#     return (o.count('o') == x.count('x'))

# My answer
def xo(s):
    return (s.lower().count('o') == s.lower().count('x'))

print(xo('xxoO'))