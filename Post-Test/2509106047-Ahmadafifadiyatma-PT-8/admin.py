import os
from prettytable import PrettyTable
import data

# Variabel global
menu_utama = ["Lihat Buku", "Tambah Buku", "Ubah Buku", "Hapus Buku", "Logout", "Keluar"]

def clear():
    os.system("cls || clear")

def tampilkan_menu():
    clear()
    print("=== MENU UTAMA ===")
    for i, menu in enumerate(menu_utama, 1):
        print(f"{i}. {menu}")

def lihat_buku(books):
    clear()
    print("=== DAFTAR BUKU ===")
    if not books:
        print("Belum ada buku yang tersimpan.")
        return False
    else:
        tabel = PrettyTable(["ID", "Judul", "Genre", "Penulis", "Tahun", "Rating", "Ulasan"])
        for id_buku, buku in books.items():
            tabel.add_row([
                id_buku, buku["judul"], buku["genre"],
                buku["penulis"], buku["tahun"], buku["rating"], buku["ulasan"]
            ])
        print(tabel)
        return True

def tambah_buku(books):
    clear()
    print("=== TAMBAH BUKU BARU ===")
    try:
        id_buku = input("ID Buku: ")
        if id_buku in books:
            print("ID sudah dipakai!")
            return False
        else:
            judul = input("Judul: ")
            genre = input("Genre: ")
            penulis = input("Penulis: ")
            tahun = input("Tahun Terbit: ")
            rating = input("Rating (1-10): ")
            ulasan = input("Ulasan: ")
            books[id_buku] = {
                "judul": judul, "genre": genre, "penulis": penulis,
                "tahun": tahun, "rating": rating, "ulasan": ulasan
            }
            print("\nBuku berhasil ditambahkan!")
            return True
    except:
        print("\nTerjadi kesalahan input.")
        return False
    input("Tekan Enter untuk kembali...")

def ubah_buku(books):
    clear()
    print("=== UBAH DATA BUKU ===")
    if not books:
        print("Belum ada buku untuk diubah.")
        input("Tekan Enter untuk kembali...")
        return False

    for id_buku, buku in books.items():
        print(f"{id_buku}. {buku['judul']}")
    pilih = input("\nMasukkan ID buku yang ingin diubah: ")

    if pilih in books:
        buku = books[pilih]
        print("Kosongkan jika tidak ingin diubah.")
        judul = input(f"Judul baru [{buku['judul']}]: ") or buku["judul"]
        genre = input(f"Genre baru [{buku['genre']}]: ") or buku["genre"]
        penulis = input(f"Penulis baru [{buku['penulis']}]: ") or buku["penulis"]
        tahun = input(f"Tahun baru [{buku['tahun']}]: ") or buku["tahun"]
        rating = input(f"Rating baru [{buku['rating']}]: ") or buku["rating"]
        ulasan = input(f"Ulasan baru [{buku['ulasan']}]: ") or buku["ulasan"]
        books[pilih] = {
            "judul": judul, "genre": genre, "penulis": penulis,
            "tahun": tahun, "rating": rating, "ulasan": ulasan
        }
        print("\nData buku berhasil diubah!")
        return True
    else:
        print("ID tidak ditemukan.")
        return False

def hapus_buku():
    clear()
    print("=== HAPUS BUKU ===")
    if not data.books:
        print("Belum ada buku yang bisa dihapus.")
    else:
        for id_buku, buku in data.books.items():
            print(f"{id_buku}. {buku['judul']}")
        hapus = input("\nMasukkan ID buku yang ingin dihapus: ")
        if hapus in data.books:
            konfirmasi = input(f"Yakin hapus '{data.books[hapus]['judul']}'? (y/n): ").lower()
            if konfirmasi == "y":
                del data.books[hapus]
                print("Buku berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("ID tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")
