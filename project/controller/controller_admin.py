from view.view_admin import tampil_data_pelanggan, tampil_data_produk
from model.database import Database
from rich.console import Console
from rich.panel import Panel

console = Console()
db = Database()

def menu_admin():
    while True:
        console.print(Panel("MENU ADMIN", style="bold magenta"))
        pilih = console.input("""
1. Lihat Semua Pelanggan
2. Lihat Semua Produk
3. Ubah Nama Pelanggan
4. Ubah Produk
5. Hapus Pelanggan
6. Hapus Produk
7. Hapus Transaksi
8. Kembali
Pilih: """)

        if pilih == "1":
            data = db.ambil_semua_pelanggan()
            tampil_data_pelanggan(data)

        elif pilih == "2":
            data = db.ambil_semua_produk()
            tampil_data_produk(data)

        elif pilih == "3":
            idp = int(console.input("ID pelanggan: "))
            nama_baru = console.input("Nama baru: ")
            db.update_pelanggan(idp, nama_baru)

        elif pilih == "4":
            idp = int(console.input("ID produk: "))
            nama = console.input("Nama baru: ")
            harga = int(console.input("Harga baru: "))
            garansi = console.input("Garansi: ")
            garansi = int(garansi) if garansi else None
            db.update_produk(idp, nama, harga, garansi)

        elif pilih == "5":
            db.hapus_pelanggan(int(console.input("ID Pelanggan: ")))

        elif pilih == "6":
            db.hapus_produk(int(console.input("ID Produk: ")))

        elif pilih == "7":
            db.hapus_transaksi(int(console.input("ID Transaksi: ")))

        else:
            break
