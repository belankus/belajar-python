#Merubah tipe data (casting)

print("===FROM STRING===")
data = "12"
print("String : ",data,type(data))
print("===TO===")
dataInt = int(data)
dataFloat = float(data)
dataBool = bool(data) # Akan bernilai True jika berisi data, dan akan false jika data kosong
print("Integer : ",dataInt,type(dataInt))
print("Float : ",dataFloat,type(dataFloat))
print("Bool : ",dataBool,type(dataBool))

print("===FROM INTEGER===")
data = -2
print("Integer : ",data,type(data))
print("===TO===")
dataStr = str(data)
dataFloat = float(data)
dataBool = bool(data) # Akan bernilai True jika berisi data bahkan minus, dan akan false jika nilai 0
print("String : ",dataStr,type(dataStr))
print("Float : ",dataFloat,type(dataFloat))
print("Bool : ",dataBool,type(dataBool))

print("===FROM FLOAT===")
data = -1.2
print("Float : ",data,type(data))
print("===TO===")
dataStr = str(data)
dataInt = int(data)
dataBool = bool(data) # Akan bernilai True jika berisi data bahkan minus, dan akan false jika nilai 0
print("String : ",dataStr,type(dataStr))
print("Integer : ",dataInt,type(dataInt))
print("Bool : ",dataBool,type(dataBool))

print("===FROM BOOLEAN===")
data = False
print("Boolean : ",data,type(data))
print("===TO===")
# Semua yang berhubungan dengan angka akan bernilai 1 jika True, dan bernilai 0 jika False
dataStr = str(data)
dataInt = int(data)
dataFloat = float(data) 
print("String : ",dataStr,type(dataStr))
print("Integer : ",dataInt,type(dataInt))
print("Float : ",dataFloat,type(dataFloat))