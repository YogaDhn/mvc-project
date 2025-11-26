from rich.console import Console
from rich.panel import Panel

console = Console()

def tampil_menu_utama():
    console.print(Panel("SISTEM TOKO ONLINE", title="PROGRAM KASIR", style="bold magenta"))
    pilihan = console.input("""
[cyan]
1. Transaksi Baru
2. Lihat Riwayat
3. Menu Admin (CRUD)
4. Keluar
Pilih: [/cyan]""")
    return pilihan
