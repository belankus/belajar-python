a = 3
b = 2
# Pertambahan +
hasil = a + b
print(a,'+',b,'=',hasil)

# Penguarangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# Exponen **
hasil = a ** b
print(a,'**',b,'=',hasil)

# Modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# Floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

'''
Prioritas Operasi
1. ()
2. Exponen **
3. Perkalian dkk * / % //
4. Penjumlahan dkk + -

'''

x = 2
y = 3
z = 4

hasil = x ** y / z *(x + y) -x % y // z

print(x,'**',y,'/',z,'*','(',x,'+',y,') -',x,'%',y,'//',z,'=',hasil)
