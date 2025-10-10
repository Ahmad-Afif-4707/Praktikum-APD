while True:
    username = input("Masukkan username: ")
    password = input("Masukkan 3 digit NIM terakhir: ")

    if username == "Afif" and password == "047":
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah, coba lagi!")

# Variabel
Aplus = 0
Amin = 0
Bplus = 0
Bmin = 0
ABplus = 0
ABmin = 0
Oplus = 0
Omin = 0

# INPUT DATA
ulang = "Y"
while ulang == "Y" or ulang == "y":
    gol = input("Golongan darah (A/B/AB/O): ")

    if gol not in ["A", "a", "B", "b", "AB", "ab", "Ab", "aB", "O", "o"]:
        print("Golongan darah tidak valid!")
        continue  

    rh = input("Rhesus (+/-): ")

    if rh not in ["+", "-"]:
        print("Rhesus tidak valid!")
        continue 

    jml = int(input("Jumlah kantong darah: "))

    # Golongan A
    if gol == "A" or gol == "a":
        if rh == "+":
            Aplus += jml * 500
        else:
            Amin += jml * 500
    # Golongan B
    elif gol == "B" or gol == "b":
        if rh == "+":
            Bplus += jml * 500
        else:
            Bmin += jml * 500
    # Golongan AB
    elif gol in ["AB", "ab", "Ab", "aB"]:
        if rh == "+":
            ABplus += jml * 500
        else:
            ABmin += jml * 500
    # Golongan O
    elif gol == "O" or gol == "o":
        if rh == "+":
            Oplus += jml * 500
        else:
            Omin += jml * 500

    ulang = input("Apakah mau input lagi (Y/T)? ")

print("=== RINGKASAN DARAH TERKUMPUL ===")
print("A+ :", Aplus, "ml")
print("A- :", Amin, "ml")
print("B+ :", Bplus, "ml")
print("B- :", Bmin, "ml")
print("AB+:", ABplus, "ml")
print("AB-:", ABmin, "ml")
print("O+ :", Oplus, "ml")
print("O-:",Omin,"ml")