import os

username_admin = "admin"
password_admin = "admin123"

def clear():
    os.system("cls || clear")

def login_admin():
    clear()
    print("=== LOGIN ADMIN ===")
    user = input("Username: ")
    pw = input("Password: ")

    if user == username_admin and pw == password_admin:
        print("\nLogin berhasil!")
        input("Tekan Enter untuk lanjut...")
        return True
    else:
        print("\nUsername atau password salah.")
        input("Tekan Enter untuk coba lagi...")
        return False

def logout_admin():
    print("\nLogout berhasil, sampai jumpa lagi!")
    input("Tekan Enter untuk kembali ke login...")
