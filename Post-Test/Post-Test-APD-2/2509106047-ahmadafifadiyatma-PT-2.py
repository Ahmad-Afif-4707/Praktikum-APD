# Suhu Celcius
suhu = [27, 33, 46, 55, 67, 92]

# Konversi suhu
# suhu_1 dan suhu_2 > Fahrenheit
fahrenheit = [(9/5) * suhu[0] + 32, (9/5) * suhu[1] + 32]

# suhu_3 dan suhu_4 > Kelvin
kelvin = [suhu[2] + 273.15, suhu[3] + 273.15]

# suhu_5 dan suhu_6 >  Reamur
reamur = [suhu[4] * 4/5, suhu[5] * 4/5]

# Jumlahkan suhu
jumlah = (fahrenheit[0] + fahrenheit[1] + kelvin[0] + kelvin[1] + reamur[0] + reamur[1])

# Rata-rata
rata2 = jumlah / 6

# Nim
NIM = 47

Boolean = NIM < ratarata

print("Suhu Celcius: ", suhu)
print("Fahrenheit: ", fahrenheit)
print("Kelvin: " , kelvin)
print("Reamur: ", reamur)
print("Jumlah semua suhu", jumlah)
print("Rata-rata suhu", rata2)
print("NIM", NIM)
print("Apakah NIM < ratarata", Boolean)
