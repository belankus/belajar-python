# Bermain dengan date time library

import datetime as dt
from dateutil.relativedelta import relativedelta

today = dt.date.today()
print(today)

hari = f'{today:%A}'
print(hari)

print('\r\n'+'HITUNG HARI LAHIR'.center(27,'='))

tanggal = int(input('Masukkan Tanggal = '))
bulan = int(input('Masukkan Bulan = '))
tahun = int(input('Masukkan Tahun = '))

tgl = dt.date(tahun,bulan,tanggal)
print(f'Anda input tanggal = {tgl}')
print(f'Anda lahir hari {tgl:%A}')

print(f'\nUmur Anda = {((dt.date.today()-tgl).days)//365} tahun')
print(f'{((dt.date.today()-tgl).days)%365//30} bulan')
print(f'{((dt.date.today()-tgl).days)%365%30} hari')

def count_year(tgl):
    today = dt.date.today()
    umur = relativedelta(today,tgl)
    return umur.years

usia = count_year(tgl)
print(f'Umur nya = {usia} tahun')