class Produk:
    def __init__(self, nama, harga):
        self.__nama = nama
        self.__harga = harga

    def tampilkan_info(self):
        print(f"Produk: {self.__nama} | Harga: Rp{self.__harga}")

    def set_harga(self, harga_baru):
        self.__harga = harga_baru

    def get_harga(self):
        return self.__harga

    def get_nama(self):
        return self.__nama
