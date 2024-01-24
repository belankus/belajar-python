# Untuk Membandingkan Nilai output boolean
'''
Operator untuk literal x = 5 , x == 5 (valid)
1. Lebih besar >
2. Lebih kecil <
3. Lebih besar sama dengan >=
4. Lebih kecil sama dengan <=
5. Sama dengan ==
6. Tidak sama dengan !=
'''

a = 3
b = 5
print("=== Lebih Dari >")
hasil = a > 4
print(a,">",4,'=',hasil)
hasil = b > 4
print(b,">",4,'=',hasil)
hasil = b > 5
print(b,">",5,'=',hasil)

print("=== Kurang Dari <")
hasil = a < 4
print(a,"<",4,'=',hasil)
hasil = b < 4
print(b,"<",4,'=',hasil)
hasil = b < 5
print(b,"<",5,'=',hasil)

print("=== Lebih Dari Sama dengan >=")
hasil = a >= 4
print(a,">=",4,'=',hasil)
hasil = b >= 4
print(b,">=",4,'=',hasil)
hasil = b >= 5
print(b,">=",5,'=',hasil)

print("=== Kurang Dari Sama dengan <=")
hasil = a <= 4
print(a,"<=",4,'=',hasil)
hasil = b <= 4
print(b,"<=",4,'=',hasil)
hasil = b <= 5
print(b,"<=",5,'=',hasil)

print("=== Sama dengan ==")
hasil = a == 4
print(a,"==",4,'=',hasil)
hasil = b == 5
print(b,"==",5,'=',hasil)

print("=== Tidak dengan !=")
hasil = a != 4
print(a,"!=",4,'=',hasil)
hasil = b != 5
print(b,"!=",5,'=',hasil)

'''
Operator untuk komparasi objek identity
1. is
2. is not

Akan membandingkan nilai objek di dalam memory
'''
print("Komparasi Object")
a = 2
b = 2

hasil = a is b
print(a,'is',b,'=',hasil)
print('id a','=',hex(id(a)))
print('id b','=',hex(id(b)))

hasil = a is not b
print(a,'is not',b,'=',hasil)
print('id a','=',hex(id(a)))
print('id b','=',hex(id(b)))