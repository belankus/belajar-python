# Aplikasi Calculator

print(20*'=')
print('Kalkulator Sederhana')
print(20*'='+'\n')

angka_1 = float(input('Masukkan angka 1 = '))
operator = input('Masukkan operator (+,-,*,/) = ')
angka_2 = float(input('Masukkan angka 2 = '))

if operator == '+':
    hasil = angka_1 + angka_2
    print(hasil)
elif operator == '-':
    hasil = angka_1 - angka_2
    print(hasil)
elif operator == '*' or operator == 'x':
    hasil = angka_1 * angka_2
    print(hasil)
elif operator == '/':
    hasil = angka_1 / angka_2
    print(hasil)
else:
    print(f' Operator {operator} tidak disupport ')