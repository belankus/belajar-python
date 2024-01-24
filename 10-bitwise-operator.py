# Melakukan operasi logika pada masing-masing bit di dalam format binary

a = 1000
b = 7

print('Nilai a =',bin(a)[2:])
print('Nilai b =',bin(b)[2:])

# Operator berikut dapat digunakan untuk operasi logika
# & (AND)
print('a & b =',bin(a&b)[2:])

# | (OR)
print('a | b =',bin(a|b)[2:])

# ^ (XOR)
print('a ^ b =',bin(a^b)[2:])


# Operator berikut cocok untuk operasi angka
# ~ (NOT) TIDAK BISA BERLAKU UNTUK OPERASI LOGIKA, hanya angka
'''Behaviour = Melakukan negasi dengan batas sebelum nol (angka negatif)|0(angka positif)'''
print('~a =',~a)

# >> (SHIFT RIGHT - Membagi nilai 2 pangkat value)
'''Original behaviour: Menggeser posisi semua bit sebanyak value mendekati nol'''
print('a >> b =',bin(a>>1)[2:])

# << (SHIFT LEFT - Mengkali nilai 2 pangkat value)
'''Original behaviour: Menggeser posisi semua bit sebanyak value menjauhi nol'''
print('a << b =',bin(a<<1)[2:])
