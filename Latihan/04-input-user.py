#Semua input pasti akan bernilai string
data = int(input("Masukkan data : "))

#Kita casting untuk mendapatkan tipe data yang diinginkan
dataInt = int(data)
dataFloat = float(data)
dataBool = bool(data)
print("Data Integer :",dataInt,type(dataInt))
print("Data Float :",dataFloat,type(dataFloat))
print("Data Boolean :",dataBool,type(dataBool)) # Akan selalu menampilkan True jika ada input, maka perlu dicasting di input