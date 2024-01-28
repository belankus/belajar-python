# Operator logika NOT, OR, AND, XOR (bitwise)

print("==== NOT ====")
a = False
print("Nilai a =",a)
print("------- NOT")
b = not a
print("Nilai not a =",b)

# OR
print("==== OR ====")
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b, '=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)

# AND
print("==== AND ====")
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)

# XOR
print("==== XOR ====")
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)