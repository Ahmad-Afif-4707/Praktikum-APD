import os

# Data login admin
username_admin = "admin"
password_admin = "admin123"

# Data awal
books = {
    1: {
        "judul": "The Lord of the Rings",
        "genre": "Fantasy",
        "penulis": "J.R.R. Tolkien",
        "tahun": "1954",
        "rating": "10",
        "ulasan": "Kisah epik penuh petualangan dan makna persahabatan."
    },
    2: {
        "judul": "The Hobbit",
        "genre": "Fantasy",
        "penulis": "J.R.R. Tolkien",
        "tahun": "1937",
        "rating": "9",
        "ulasan": "Cerita petualangan yang ringan dan menyenangkan."
    }
}
book_id = len(books)

# LOGIN
while True:
    os.system("cls || clear")
    print("=== LOGIN ADMIN ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == username_admin and password == password_admin:
        print("Login berhasil!")
        input("Tekan Enter untuk masuk ke menu...")
        break
    else:
        print("Username atau password salah!")
        input("Tekan Enter untuk coba lagi...")

# MENU UTAMA
while True:
    os.system("cls || clear")
    print("=== KOLEKSI BUKU PRIBADI ===")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Ubah Buku")
    print("4. Hapus Buku")
    print("5. Logout")
    print("6. Keluar Program")
    menu = input("Pilih menu (1-6): ")

    # CREATE
    if menu == "1":
        os.system("cls || clear")
        print("=== TAMBAH BUKU ===")
        judul = input("Judul: ")
        genre = input("Genre: ")
        penulis = input("Penulis: ")
        tahun = input("Tahun Terbit: ")
        rating = input("Rating (1-10): ")
        ulasan = input("Ulasan: ")

        book_id += 1
        books[book_id] = {
            "judul": judul,
            "genre": genre,
            "penulis": penulis,
            "tahun": tahun,
            "rating": rating,
            "ulasan": ulasan
        }

        print("Buku berhasil ditambahkan!")
        input("Tekan Enter untuk lanjut...")

    # READ
    elif menu == "2":
        os.system("cls || clear")
        print("=== DAFTAR BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            for id, b in books.items():
                print(f"{id}. {b['judul']} ({b['genre']}) - {b['penulis']}")
                print(f"   Tahun: {b['tahun']}, Rating: {b['rating']}/10")
                print(f"   Ulasan: {b['ulasan']}")
                print("-" * 40)
        input("Tekan Enter untuk lanjut...")

    # UPDATE
    elif menu == "3":
        os.system("cls || clear")
        print("=== UBAH DATA BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            for id, b in books.items():
                print(f"{id}. {b['judul']}")
            ubah = input("Masukkan ID buku yang ingin diubah: ")

            if ubah.isdigit() and int(ubah) in books:
                ubah = int(ubah)
                print("Kosongkan jika tidak ingin diubah.")
                judul = input("Judul baru: ") or books[ubah]["judul"]
                genre = input("Genre baru: ") or books[ubah]["genre"]
                penulis = input("Penulis baru: ") or books[ubah]["penulis"]
                tahun = input("Tahun baru: ") or books[ubah]["tahun"]
                rating = input("Rating baru: ") or books[ubah]["rating"]
                ulasan = input("Ulasan baru: ") or books[ubah]["ulasan"]

                books[ubah] = {
                    "judul": judul,
                    "genre": genre,
                    "penulis": penulis,
                    "tahun": tahun,
                    "rating": rating,
                    "ulasan": ulasan
                }
                print("Data berhasil diperbarui!")
            else:
                print("ID buku tidak valid.")
        input("Tekan Enter untuk lanjut...")

    # DELETE
    elif menu == "4":
        os.system("cls || clear")
        print("=== HAPUS DATA BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            for id, b in books.items():
                print(f"{id}. {b['judul']}")
            hapus = input("Masukkan ID buku yang ingin dihapus: ")

            if hapus.isdigit() and int(hapus) in books:
                del books[int(hapus)]
                print("Buku berhasil dihapus!")
            else:
                print("ID tidak valid.")
        input("Tekan Enter untuk lanjut...")

    # LOGOUT
    elif menu == "5":
        os.system("cls || clear")
        print("Anda telah logout.")
        input("Tekan Enter untuk kembali ke login...")
        while True:
            os.system("cls || clear")
            print("=== LOGIN ADMIN ===")
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            if username == username_admin and password == password_admin:
                print("Login berhasil!")
                input("Tekan Enter untuk kembali ke menu...")
                break
            else:
                print("Username atau password salah!")
                input("Tekan Enter untuk coba lagi...")

    # EXIT
    elif menu == "6":
        os.system("cls || clear")
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")
