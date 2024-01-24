# Gabungan ++++3----10++++

print('=== Gabungan ===')

inputUser = float(input('Masukkan angka : '))

isKurangDari = (inputUser < 3)
print('Kurang dari 3 =',isKurangDari)

isLebihDari = (inputUser > 10)
print('Lebih dari 10 =',isLebihDari)

isCorrect = isKurangDari or isLebihDari
print('Angka yang dimasukkan :',isCorrect)

print('\n',10*'=','\n')

# Irisan ----3++++10----

print('=== Irisan ===')

inputUser = float(input('Masukkan angka : '))

isLebihDari = (inputUser > 3)
print('Lebih dari 3 =',isLebihDari)

isKurangDari = (inputUser < 10)
print('Kurang dari 10 =',isKurangDari)

isCorrect = isKurangDari and isLebihDari
print('Angka yang dimasukkan :',isCorrect)

print('\n',10*'=','\n')


'''
Tugas Rumah PR
1. ----0++++5----8++++11----
2. ++++0----5++++8----11++++
'''

# Penyelesaian soal 1
# Perpaduan irisan dan gabungan

print("=== SOAL LATIHAN 1 ===\n")

print('----0++++5----8++++11----')
inputUser = float(input("Masukkan angka : "))

# Irisan 1
# ----0+++5----
# ----0++++
isLebihDari0 = (inputUser > 0)
print('0++++           =',isLebihDari0)
# ++++5----
isKurangDari5 = (inputUser < 5)
print('++++5           =',isKurangDari5)
## ----0++++5----
irisan1 = isLebihDari0 and isKurangDari5
print('----0++++5----  =',irisan1)

# Irisan 2
# ----8++++11----
# ----8++++
isLebihDari8 = (inputUser > 8)
print('8++++           =',isLebihDari8)
# ++++5----
isKurangDari11 = (inputUser < 11)
print('++++11          =',isKurangDari11)
## ----8++++11----
irisan2 = isLebihDari8 and isKurangDari11
print('----8++++11---- =',irisan2)

### Final Result
isCorrect = irisan1 or irisan2
print('Angka yang dimasukkan =',isCorrect)

print('\n',10*'=','\n')

# Penyelesaian soal 2
# Perpaduan gabungan dan irisan

print("=== SOAL LATIHAN 2 ===\n")

print('++++0----5++++8----11++++')
inputUser = float(input("Masukkan angka : "))

# Gabungan 1
# ++++0----5++++
# ++++0
isKurangDari0 = (inputUser < 0)
print('++++0 =',isKurangDari0)

# 5++++
isLebihDari5 = (inputUser > 5)
print('5++++ =',isLebihDari5)

# ++++0----5++++
gabungan1 = isKurangDari0 or isLebihDari5
print('++++0----5++++ =',gabungan1)

# Gabungan 2
# ++++8----11++++
# ++++8
isKurangDari8 = (inputUser < 8)
print('++++8 =',isKurangDari8)

# 11++++
isLebihDari11 = (inputUser > 11)
print('8++++ =',isLebihDari11)

# ++++8----11++++
gabungan2 = isKurangDari8 or isLebihDari11
print('++++8----11++++ =',gabungan2)

# Final Result
isCorrect = gabungan1 and gabungan2
print('Angka yang dimasukkan =',isCorrect)