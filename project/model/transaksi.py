from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from model.elektronik import Elektronik

console = Console()

class Transaksi:
    def __init__(self, pelanggan, produk_list):
        self.pelanggan = pelanggan
        self.produk_list = produk_list

    def hitung_total(self):
        return sum([p.get_harga() for p in self.produk_list])

    def tampilkan_struk(self):
        console.print(f"[bold cyan]Pelanggan:[/bold cyan] {self.pelanggan.nama}")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("No", justify="center")
        table.add_column("Nama Produk", justify="left")
        table.add_column("Harga", justify="right")
        table.add_column("Garansi", justify="center")

        for i, p in enumerate(self.produk_list, start=1):
            garansi_text = f"{p.garansi} tahun" if isinstance(p, Elektronik) else "-"
            table.add_row(str(i), p.get_nama(), f"Rp {p.get_harga():,}", garansi_text)

        console.print(table)

        total = self.hitung_total()
        console.print(Panel(f"[bold yellow]Total Pembayaran: Rp {total:,}[/bold yellow]", border_style="green"))
