# Memberikan Alignment Pada Text

nama = 'Bellawan Kusuma Aji'
umur = 23
kelas = '10 IPA 8'

print('\r\n'+'DATA SISWA'.center(30,'='))
data = f'''
Nama  = {nama:>20}
Umur  = {umur:>20}
Kelas = {kelas:>20}

'''

print(data)