import login
import admin

while True:
    if not login.login_admin():
        continue

    while True:
        login.clear()
        print("=== MENU UTAMA ===")
        print("1. Lihat Buku")
        print("2. Tambah Buku")
        print("3. Ubah Buku")
        print("4. Hapus Buku")
        print("5. Logout")
        print("6. Keluar")

        pilih = input("Pilih menu (1-6): ")

        if pilih == "1":
            admin.lihat_buku()
        elif pilih == "2":
            admin.tambah_buku()
        elif pilih == "3":
            admin.ubah_buku()
        elif pilih == "4":
            admin.hapus_buku()
        elif pilih == "5":
            print("\nLogout berhasil.")
            break
        elif pilih == "6":
            print("\nTerima kasih telah menggunakan program ini.")
            exit()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")
