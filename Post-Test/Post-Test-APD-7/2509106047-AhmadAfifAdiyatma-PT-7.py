import os

books = {
    1: {
        "judul": "The Lord of the Rings",
        "genre": "Fantasi",
        "penulis": "J.R.R. Tolkien",
        "tahun": "1954",
        "rating": "10",
        "ulasan": "Kisah epik petualangan dan makna persahabatan."
    },
    2: {
        "judul": "The Hobbit",
        "genre": "Petualangan",
        "penulis": "J.R.R. Tolkien",
        "tahun": "1937",
        "rating": "9",
        "ulasan": "Cerita petualangan yang ringan dan menyenangkan."
    }
}
username_admin = "admin"
password_admin = "admin123"

def clear_screen():
    os.system("cls || clear")

def tampilkan_menu():
    print("\n=== KOLEKSI BUKU PRIBADI ===")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Ubah Buku")
    print("4. Hapus Buku")
    print("5. Logout")
    print("6. Keluar")

def login():
    clear_screen()
    print("=== LOGIN ADMIN ===")
    user = input("Username: ")
    pw = input("Password: ")
    return user == username_admin and pw == password_admin

def tambah_buku():
    clear_screen()
    print("=== TAMBAH BUKU ===")
    try:
        judul = input("Judul: ")
        genre = input("Genre: ")
        penulis = input("Penulis: ")
        tahun = input("Tahun Terbit: ")
        rating = input("Rating (1-10): ")
        ulasan = input("Ulasan: ")
        id_baru = len(books) + 1
        books[id_baru] = {
            "judul": judul,
            "genre": genre,
            "penulis": penulis,
            "tahun": tahun,
            "rating": rating,
            "ulasan": ulasan
        }
        print("Buku berhasil ditambahkan!")
    except Exception as e:
        print("Terjadi kesalahan:", e)
    input("Tekan Enter untuk lanjut...")

def lihat_buku():
    clear_screen()
    print("=== DAFTAR BUKU ===")
    if not books:
        print("Belum ada buku.")
    else:
        for id, data in books.items():
            print(f"{id}. {data['judul']} ({data['genre']}) - {data['penulis']}")
            print(f"   Tahun: {data['tahun']}, Rating: {data['rating']}/10")
            print(f"   Ulasan: {data['ulasan']}")
            print("-" * 40)
    input("Tekan Enter untuk lanjut...")

def ubah_buku():
    clear_screen()
    print("=== UBAH DATA BUKU ===")
    if not books:
        print("Belum ada buku.")
    else:
        try:
            for id, data in books.items():
                print(f"{id}. {data['judul']}")
            pilih = int(input("Masukkan ID buku: "))
            if pilih in books:
                b = books[pilih]
                b["judul"] = input("Judul baru: ") or b["judul"]
                b["genre"] = input("Genre baru: ") or b["genre"]
                b["penulis"] = input("Penulis baru: ") or b["penulis"]
                b["tahun"] = input("Tahun baru: ") or b["tahun"]
                b["rating"] = input("Rating baru: ") or b["rating"]
                b["ulasan"] = input("Ulasan baru: ") or b["ulasan"]
                print("Data buku berhasil diubah!")
            else:
                print("ID tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
    input("Tekan Enter untuk lanjut...")

def hapus_buku():
    clear_screen()
    print("=== HAPUS DATA BUKU ===")
    if not books:
        print("Belum ada buku.")
    else:
        try:
            for id, data in books.items():
                print(f"{id}. {data['judul']}")
            hapus = int(input("Masukkan ID buku yang ingin dihapus: "))
            if hapus in books:
                del books[hapus]
                print("Buku berhasil dihapus!")
            else:
                print("ID tidak valid.")
        except ValueError:
            print("Input harus berupa angka!")
    input("Tekan Enter untuk lanjut...")

while True:
    if login():
        while True:
            clear_screen()
            tampilkan_menu()
            menu = input("Pilih menu: ")

            if menu == "1":
                tambah_buku()
            elif menu == "2":
                lihat_buku()
            elif menu == "3":
                ubah_buku()
            elif menu == "4":
                hapus_buku()
            elif menu == "5":
                print("Anda telah logout.")
                input("Tekan Enter untuk kembali ke login...")
                break
            elif menu == "6":
                print("Terima kasih telah menggunakan program ini!")
                exit()
            else:
                print("Pilihan tidak valid!")
                input("Tekan Enter untuk lanjut...")
    else:
        print("Username atau password salah!")
        input("Tekan Enter untuk coba lagi...")
