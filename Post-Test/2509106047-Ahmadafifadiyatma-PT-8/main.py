import login
import admin
import data
import inquirer

while True:
    if not login.login_admin():
        continue

    while True:
        pertanyaan = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "Lihat Buku",
                    "Tambah Buku",
                    "Ubah Buku",
                    "Hapus Buku",
                    "Logout",
                    "Keluar"
                ],
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        pilihan = jawaban["menu"]

        if pilihan == "Lihat Buku":
            if admin.lihat_buku(data.books):
                print("\nData buku berhasil ditampilkan.")
            else:
                print("\nTidak ada buku untuk ditampilkan.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "Tambah Buku":
            if admin.tambah_buku(data.books):
                print("\nBuku baru berhasil disimpan.")
            else:
                print("\nGagal menambah buku.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "Ubah Buku":
            if admin.ubah_buku(data.books):
                print("\nData buku berhasil diperbarui.")
            else:
                print("\nTidak ada yang diubah.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "Hapus Buku":
            admin.hapus_buku()

        elif pilihan == "Logout":
            login.logout_admin()
            break

        elif pilihan == "Keluar":
            print("\nTerima kasih sudah menggunakan program ini!")
            exit()
