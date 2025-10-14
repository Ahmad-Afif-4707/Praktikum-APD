import os

books = []

while True:
    os.system("cls || clear")
    print("=== KOLEKSI BUKU PRIBADI ===")
    print("1. Tambah Buku")
    print("2. Lihat Buku")
    print("3. Ubah Buku")
    print("4. Hapus Buku")
    print("5. Keluar")
    menu = input("Pilih menu: ")

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
        buku = [judul, genre, penulis, tahun, rating, ulasan]
        books.append(buku)
        print("Buku berhasil ditambahkan!")
        input("Tekan Enter untuk lanjut...")

    # READ
    elif menu == "2":
        os.system("cls || clear")
        print("=== DAFTAR BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            nomor = 1
            for b in books:
                print(f"{nomor}. {b[0]} ({b[1]}) - {b[2]}")
                print(f"   Tahun: {b[3]}, Rating: {b[4]}/10")
                print(f"   Ulasan: {b[5]}")
                print("-" * 40)
                nomor += 1
        input("Tekan Enter untuk lanjut...")

    # UPDATE
    elif menu == "3":
        os.system("cls || clear")
        print("=== UBAH DATA BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            for i in range(len(books)):
                print(f"{i+1}. {books[i][0]}")
            ubah = int(input("Pilih nomor buku: ")) - 1
            if 0 <= ubah < len(books):
                print("Kosongkan jika tidak ingin diubah.")
                judul = input("Judul baru: ") or books[ubah][0]
                genre = input("Genre baru: ") or books[ubah][1]
                penulis = input("Penulis baru: ") or books[ubah][2]
                tahun = input("Tahun baru: ") or books[ubah][3]
                rating = input("Rating baru: ") or books[ubah][4]
                ulasan = input("Ulasan baru: ") or books[ubah][5]
                books[ubah] = [judul, genre, penulis, tahun, rating, ulasan]
                print("Data berhasil diperbarui!")
            else:
                print("Nomor tidak valid.")
        input("Tekan Enter untuk lanjut...")

    # DELETE
    elif menu == "4":
        os.system("cls || clear")
        print("=== HAPUS DATA BUKU ===")
        if len(books) == 0:
            print("Belum ada buku.")
        else:
            for i in range(len(books)):
                print(f"{i+1}. {books[i][0]}")
            hapus = int(input("Pilih nomor buku: ")) - 1
            if 0 <= hapus < len(books):
                del books[hapus]
                print("Buku berhasil dihapus!")
            else:
                print("Nomor tidak valid.")
        input("Tekan Enter untuk lanjut...")

    # EXIT
    elif menu == "5":
        os.system("cls || clear")
        print("Terima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")