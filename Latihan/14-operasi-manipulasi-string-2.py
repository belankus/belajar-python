# Method pada string
## Upper Case

nama = "ajisaka pyutra lestari"

print(nama.upper())

## Upper Case
namaa = "ini Alazy AsYikin Ajah"

print(namaa.lower())

print(nama.islower())

##startswith
print(nama.startswith('aji'))

##endswith
print(nama.endswith('ari'))

## Join Split
nama = ['aku', 'adalah', 'masbel']

print(nama)
gabung = ' '.join(nama)
print(gabung)

pisah = gabung.split(' ')
print(pisah)

## Alokasi karakter ljust(), rjust(), center()
kanan = 'kanan'.rjust(10)
print("'"+kanan+"'")

kiri = 'kiri'.ljust(10)
print("'"+kiri+"'")

tengah = 'tengah'.center(20,'=')
print("'"+tengah+"'")

# Menghapus strip
tengah = tengah.strip('=')
print("'"+tengah+"'")

## Method lain
'''
isapha() = untuk menecek semuanya huruf
isalnum() = untuk mengecek huruf dan angka
isdecimal() = angka saja
isspace() = spasi, tab, new line
istitle() = semua kata diawali huruf besar
'''
