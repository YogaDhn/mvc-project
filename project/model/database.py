import sqlite3

class Database:
    def __init__(self, db_name="toko_online.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.buat_tabel()

    def buat_koneksi(self):
        return sqlite3.connect(self.db_name)

    def buat_tabel(self):
        with self.conn:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pelanggan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL
            )
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produk (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT NOT NULL,
                harga INTEGER NOT NULL,
                garansi INTEGER
            )
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transaksi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pelanggan INTEGER,
                total INTEGER,
                FOREIGN KEY(id_pelanggan) REFERENCES pelanggan(id)
            )
            """)
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS detail_transaksi (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_transaksi INTEGER,
                id_produk INTEGER,
                FOREIGN KEY(id_transaksi) REFERENCES transaksi(id),
                FOREIGN KEY(id_produk) REFERENCES produk(id)
            )
            """)

    #CREATE
    def simpan_pelanggan(self, nama):
        with self.conn:
            self.cursor.execute("INSERT INTO pelanggan (nama) VALUES (?)", (nama,))
        return self.cursor.lastrowid

    def simpan_produk(self, nama, harga, garansi=None):
        with self.conn:
            self.cursor.execute(
                "INSERT INTO produk (nama, harga, garansi) VALUES (?, ?, ?)",
                (nama, harga, garansi)
            )
        return self.cursor.lastrowid

    def simpan_transaksi(self, id_pelanggan, total):
        with self.conn:
            self.cursor.execute(
                "INSERT INTO transaksi (id_pelanggan, total) VALUES (?, ?)",
                (id_pelanggan, total)
            )
        return self.cursor.lastrowid

    def simpan_detail(self, id_transaksi, id_produk):
        with self.conn:
            self.cursor.execute(
                "INSERT INTO detail_transaksi (id_transaksi, id_produk) VALUES (?, ?)",
                (id_transaksi, id_produk)
            )

    # READ
    def ambil_semua_pelanggan(self):
        self.cursor.execute("SELECT * FROM pelanggan")
        return self.cursor.fetchall()

    def ambil_semua_produk(self):
        self.cursor.execute("SELECT * FROM produk")
        return self.cursor.fetchall()

    def ambil_semua_transaksi(self):
        self.cursor.execute("""
        SELECT t.id, p.nama, t.total
        FROM transaksi t
        JOIN pelanggan p ON t.id_pelanggan = p.id
        ORDER BY t.id DESC
        """)
        return self.cursor.fetchall()


    #UPDATE
    def update_pelanggan(self, id, nama_baru):
        with self.conn:
            self.cursor.execute("UPDATE pelanggan SET nama = ? WHERE id = ?", (nama_baru, id))

    def update_produk(self, id, nama, harga, garansi=None):
        with self.conn:
            self.cursor.execute(
                "UPDATE produk SET nama = ?, harga = ?, garansi = ? WHERE id = ?",
                (nama, harga, garansi, id)
            )

    # DELETE
    def hapus_pelanggan(self, id):
        with self.conn:
            self.cursor.execute("DELETE FROM pelanggan WHERE id = ?", (id,))

    def hapus_produk(self, id):
        with self.conn:
            self.cursor.execute("DELETE FROM produk WHERE id = ?", (id,))

    def hapus_transaksi(self, id):
        with self.conn:
            self.cursor.execute("DELETE FROM transaksi WHERE id = ?", (id,))
            self.cursor.execute("DELETE FROM detail_transaksi WHERE id_transaksi = ?", (id,))

    def tutup(self):
        self.conn.close()
