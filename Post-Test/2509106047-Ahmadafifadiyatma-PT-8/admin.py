import os
from prettytable import PrettyTable
import data

def clear():
    os.system("cls || clear")

def lihat_buku():
    clear()
    print("=== DAFTAR BUKU ===")
    if not data.books:
        print("Belum ada buku yang tersimpan.")
    else:
        tabel = PrettyTable(["ID", "Judul", "Genre", "Penulis", "Tahun", "Rating", "Ulasan"])
        for id_buku, buku in data.books.items():
            tabel.add_row([id_buku, buku["judul"], buku["genre"], buku["penulis"], buku["tahun"], buku["rating"], buku["ulasan"]])
        print(tabel)
    input("\nTekan Enter untuk kembali ke menu...")

def tambah_buku():
    clear()
    print("=== TAMBAH BUKU ===")
    id_buku = input("Masukkan ID buku: ")
    if id_buku in data.books:
        print("ID sudah digunakan!")
    else:
        judul = input("Judul: ")
        genre = input("Genre: ")
        penulis = input("Penulis: ")
        tahun = input("Tahun Terbit: ")
        rating = input("Rating (1-10): ")
        ulasan = input("Ulasan: ")
        data.books[id_buku] = {
            "judul": judul,
            "genre": genre,
            "penulis": penulis,
            "tahun": tahun,
            "rating": rating,
            "ulasan": ulasan
        }
        print("Buku berhasil ditambahkan!")
    input("\nTekan Enter untuk kembali...")

def ubah_buku():
    clear()
    print("=== UBAH BUKU ===")
    if not data.books:
        print("Belum ada buku.")
    else:
        lihat_buku()
        pilih = input("Masukkan ID buku yang ingin diubah: ")
        if pilih in data.books:
            buku = data.books[pilih]
            print("Kosongkan jika tidak ingin diubah.")
            judul = input(f"Judul baru [{buku['judul']}]: ") or buku["judul"]
            genre = input(f"Genre baru [{buku['genre']}]: ") or buku["genre"]
            penulis = input(f"Penulis baru [{buku['penulis']}]: ") or buku["penulis"]
            tahun = input(f"Tahun baru [{buku['tahun']}]: ") or buku["tahun"]
            rating = input(f"Rating baru [{buku['rating']}]: ") or buku["rating"]
            ulasan = input(f"Ulasan baru [{buku['ulasan']}]: ") or buku["ulasan"]
            data.books[pilih] = {
                "judul": judul,
                "genre": genre,
                "penulis": penulis,
                "tahun": tahun,
                "rating": rating,
                "ulasan": ulasan
            }
            print("Data berhasil diperbarui!")
        else:
            print("ID buku tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")

def hapus_buku():
    clear()
    print("=== HAPUS BUKU ===")
    if not data.books:
        print("Belum ada buku.")
    else:
        lihat_buku()
        hapus = input("Masukkan ID buku yang ingin dihapus: ")
        if hapus in data.books:
            konfirmasi = input(f"Yakin ingin menghapus '{data.books[hapus]['judul']}'? (y/n): ").lower()
            if konfirmasi == "y":
                del data.books[hapus]
                print("Buku berhasil dihapus!")
            else:
                print("Penghapusan dibatalkan.")
        else:
            print("ID tidak ditemukan.")
    input("\nTekan Enter untuk kembali...")
