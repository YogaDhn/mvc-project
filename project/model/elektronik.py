from model.produk import Produk

class Elektronik(Produk):
    def __init__(self, nama, harga, garansi):
        super().__init__(nama, harga)
        self.garansi = garansi

    def tampilkan_info(self):
        print(f"Elektronik: {self.get_nama()} | Garansi: {self.garansi} tahun | Harga: Rp{self.get_harga()}")
