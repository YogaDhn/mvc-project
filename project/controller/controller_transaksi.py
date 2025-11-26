from model.pelanggan import Pelanggan
from model.produk import Produk
from model.elektronik import Elektronik
from model.transaksi import Transaksi
from model.database import Database
from view.view_transaksi import tampilkan_riwayat_transaksi
from rich.console import Console
from rich.panel import Panel

console = Console()
db = Database()

def transaksi_baru():
    nama = console.input("Nama pelanggan: ")
    pelanggan = Pelanggan(nama)
    id_pelanggan = db.simpan_pelanggan(nama)

    produk_list = []

    while True:
        jenis = console.input("Jenis produk (1=normal, 2=elektronik): ")

        nama_p = console.input("Nama produk: ")
        harga = int(console.input("Harga: "))

        if jenis == "2":
            garansi = int(console.input("Garansi tahun: "))
            p = Elektronik(nama_p, harga, garansi)
            idp = db.simpan_produk(nama_p, harga, garansi)
        else:
            p = Produk(nama_p, harga)
            idp = db.simpan_produk(nama_p, harga, None)

        produk_list.append((p, idp))

        again = console.input("Tambah lagi? (y/n): ")
        if again.lower() != "y":
            break

    trans = Transaksi(pelanggan, [p[0] for p in produk_list])
    total = trans.hitung_total()
    id_transaksi = db.simpan_transaksi(id_pelanggan, total)

    for p in produk_list:
        db.simpan_detail(id_transaksi, p[1])

    trans.tampilkan_struk()
    console.print(Panel("Transaksi berhasil disimpan!", style="green"))

def tampilkan_riwayat():
    data = db.ambil_semua_transaksi()
    tampilkan_riwayat_transaksi(data)
