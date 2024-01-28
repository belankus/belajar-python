# operasi string
# 1. Concatenate

first_name = 'ucup'
middle = 'D'
last_name = 'Luffy'

nama = first_name + ' '+ middle+' ' + last_name

print(nama)

# 2. Menghitung Panjang
print(len(nama))

# 3. Operator string
# Mengecek string apakah ada dalam string lain

d = 'D'

status = d in nama
print(status)

# Mengecek string apakah tidak ada

e = 'e'

status = e not in nama
print(status)

# Mengulang string
print(10*'wk')

# Indexing Ambil data dari string
print(nama[0]) #Ambil karakter dari index 0
print(nama[-1]) #Ambil karakter dari belakang

# Slicing data
print(nama[0:4])

# Item paling kecil
print(min(nama))

# Item paling besar
print(max(nama))

#ASCII code
print(ord(min(nama)))

#ASCII code
print(ord(max(nama)))

#ASCII code covert
print(chr(121))

# Operator dalam bentuk method

hitung = nama.count('u')
print(hitung)