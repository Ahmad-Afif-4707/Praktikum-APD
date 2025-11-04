import os

def clear():
    os.system("cls || clear")

def login_admin():
    clear()
    print("=== LOGIN ADMIN ===")
    user = input("Masukkan username: ")
    pw = input("Masukkan password: ")

    if user == "admin" and pw == "admin123":
        print("\nLogin berhasil! Selamat datang.")
        input("Tekan Enter untuk lanjut...")
        return True
    else:
        print("\nUsername atau password salah.")
        input("Tekan Enter untuk coba lagi...")
        return False