from view.view_main import tampil_menu_utama
from controller.controller_transaksi import transaksi_baru, tampilkan_riwayat
from controller.controller_admin import menu_admin
from model.database import Database

db = Database()

def run():
    while True:
        pilih = tampil_menu_utama()

        if pilih == "1":
            transaksi_baru()

        elif pilih == "2":
            tampilkan_riwayat()

        elif pilih == "3":
            menu_admin()

        elif pilih == "4":
            db.tutup()
            break
