# String adalah kumpulan karakter (huruf, angka, simbol)

'''
Cara membuat string :
1. Double quote "..."
2. Single quote '...'
'''

a = "Apa yang kamu lakukan?"
b = 'Belajar Python'

print(a)
print(b)

# Meletakkan quote dalam string

c = "'Ini single Quote'"
d = '"Ini double quote"'
e = "Ini hari jum'at"

print(c)
print(d)
print(e)

# Escape character didefinisikan dengan backslash \
f = 'Ah bagaimana jika Pak Sa\'ad marah'

print(f)
print('C:\\new')


'''
Beberapa contoh escape character
\t untuk menambahkan tab
\r untuk cariage return (agar cursor kembali ke awal halaman) CR - Cariage Return
\n untuk menambahkan line baru (enter) LF - Line Feed
** Biasanya \r\n dikombinasikan CRLF - Cariage Return Line Feed
f'...' RAW String untuk nonaktifkan semua escape karakter
'''
#RAW string
print(r"kelihatannya sih bakal hari jum'at\new year")


#tab
g = 'Harga\t:\tRp2.000'
print(g)

#new line
h = 'Apa kabar Lan?\r\nAlhamdulillah Ya, kita sudah merdeka'
print(h)

# multiline raw string (non aktifkan semua escape character)
i = r'''
bagaimana pak haji, obrolan kemarin?
Alhamdulillah Pak, akhirnya ada mufakat
Syukurlah kalau begitu Pak
jadi C:\nama
'''
print(i)