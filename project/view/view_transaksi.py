from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def tampilkan_riwayat_transaksi(data):
    if not data:
        console.print("[red]Belum ada transaksi.[/red]")
        return

    table = Table(title="Riwayat Transaksi")
    table.add_column("ID")
    table.add_column("Pelanggan")
    table.add_column("Total")

    for t in data:
        table.add_row(str(t[0]), t[1], f"Rp {t[2]:,}")

    console.print(table)
