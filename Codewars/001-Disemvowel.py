# Link https://www.codewars.com/kata/52fba66badcd10859f00097e

# My Code
# def disemvowel(string_):
#     string = string_
#     string_ = ''
#     for x in string:
#         a = 'AIUEOaiueo'
#         for y in a:
#             if x == y:
#                 x = ''
#         string_ += x
#     return string_

# Best practice
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")

print(disemvowel('Bellawan Kusuma Aji'))