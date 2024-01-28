# Format String
'''
Digunakan untuk mempermudah menyambung string dengan variabel lain yang berbeda tipe data tanpa harus casting

'''

umur = 25

data = f"nama saya adalah Bellawan. saya berumur {umur} tahun"
print(data)

harsat = 15200
jumlah = 13

data = f"""
Harga Satuan 
Harga total adalah = Rp {harsat*jumlah:,.2f}"""
print(data)