username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == "Afif":
    if password == "047":
        print("=== Kalkulator Konversi SI ===")
        print("1. Kaki → Meter")
        print("2. Kilometer → Meter")
        print("3. Centimeter → Meter")
        print("4. Pon → Kilogram")
        print("5. Ton → Kilogram")
        print("6. Gram → Kilogram")
        print("7. Celcius → Kelvin")
        print("8. Fahrenheit → Kelvin")
        print("9. Reamur → Kelvin")
        print("10. Menit → Detik")
        print("11. Jam → Detik")

        pilihan = input("Pilih konversi (1-11): ")

        if pilihan == "1":
            nilai = float(input("Masukkan nilai (ft): "))
            print("Hasil =", nilai * 0.3048, "meter")
        elif pilihan == "2":
            nilai = float(input("Masukkan nilai (km): "))
            print("Hasil =", nilai * 1000, "meter")
        elif pilihan == "3":
            nilai = float(input("Masukkan nilai (cm): "))
            print("Hasil =", nilai / 100, "meter")
        elif pilihan == "4":
            nilai = float(input("Masukkan nilai (lb): "))
            print("Hasil =", nilai * 0.453592, "kg")
        elif pilihan == "5":
            nilai = float(input("Masukkan nilai (ton): "))
            print("Hasil =", nilai * 1000, "kg")
        elif pilihan == "6":
            nilai = float(input("Masukkan nilai (g): "))
            print("Hasil =", nilai / 1000, "kg")
        elif pilihan == "7":
            nilai = float(input("Masukkan nilai (°C): "))
            print("Hasil =", nilai + 273.15, "K")
        elif pilihan == "8":
            nilai = float(input("Masukkan nilai (°F): "))
            print("Hasil =", (nilai - 32) * 5/9 + 273.15, "K")
        elif pilihan == "9":
            nilai = float(input("Masukkan nilai (°Re): "))
            print("Hasil =", nilai * 5/4 + 273.15, "K")
        elif pilihan == "10":
            nilai = float(input("Masukkan nilai (menit): "))
            print("Hasil =", nilai * 60, "detik")
        elif pilihan == "11":
            nilai = float(input("Masukkan nilai (jam): "))
            print("Hasil =", nilai * 3600, "detik")
        else:
            print("Pilihan tidak valid!")

    else:
        print("Password salah!")
else:
    print("Username salah!")