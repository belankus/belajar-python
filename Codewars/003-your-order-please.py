# Link : https://www.codewars.com/kata/55c45be3b2079eccff00010f

'''
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Example :
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

#  My answer
def order(sentence):
  dump = sentence.split()
  sentence = sentence.split()
  number = '123456789'
  for x in sentence:
     for y in x:
        if y in number:
           dump[int(y)-1] = x

  return ' '.join(dump)

# Jawaban lain
'''
def order(sentence):
    data = sentence.split()

    result = []

    for word in data:
        for letter in word:
            if letter.isdigit():
                result.append([int(letter), word])

    return " ".join([x[1] for x in sorted(result)])

'''
        
    

#   return sentence

print(order(''))