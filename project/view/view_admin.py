from rich.console import Console
from rich.table import Table

console = Console()

def tampil_data_pelanggan(data):
    table = Table(title="Data Pelanggan", header_style="bold green")
    table.add_column("ID", justify="center")
    table.add_column("Nama", justify="left")
    for p in data:
        table.add_row(str(p[0]), p[1])
    console.print(table)

def tampil_data_produk(data):
    table = Table(title="Data Produk", header_style="bold cyan")
    table.add_column("ID")
    table.add_column("Nama")
    table.add_column("Harga")
    table.add_column("Garansi")
    for p in data:
        table.add_row(str(p[0]), p[1], f"Rp {p[2]:,}", str(p[3] or "-"))
    console.print(table)
