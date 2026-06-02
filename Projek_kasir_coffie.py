# Analis data penjualan sederhana
# Mencari harga terendah dari semua harga
# data nama kofie
data_cofie = [
    {"nama_barang": "Espresso", "harga": 18000},
    {"nama_barang": "Americano", "harga": 20000},
    {"nama_barang": "Cappuccino", "harga": 25000},
    {"nama_barang": "Latte", "harga": 27000},
    {"nama_barang": "Mocha", "harga": 30000},
    {"nama_barang": "Caramel Macchiato", "harga": 32000},
    {"nama_barang": "Cold Brew", "harga": 28000}
]

# data penyimpan  
coffie_pesanan = []
coffie_harga = []
total_harga = 0

# Tampilkan menu nya
for nomor, coffie in enumerate(data_cofie, start=1):
    print(f'{nomor}. {coffie["nama_barang"]:<18} Rp.{coffie["harga"]:,}')
print("0. Untuk selesai")

# Pilih menu
print(" ") # Untuk memberikan jarak dari daftar menu
while True:
    pilih_menu = int(input("Pilih Menu: ")) # Harus menggunakan index
    # Unutk keluar program
    if pilih_menu == 0:
        break

    barang_pilihan = data_cofie[pilih_menu - 1] # untuk mengambil data dari menu

    # Di simpan ke keranjang
    coffie_pesanan.append(barang_pilihan)

    # Menghitung jumblah harga
    total_harga += coffie["harga"]
    print("Berhasil Di Pilih ✅ \n")

print("=="*13)
print("==== STRUK PEMBELIAN ====")
print("=="*13)
print(" ")

print(f"{'No':<3} {'Nama':<15} {'Harga'}")
for no, nama in enumerate(coffie_pesanan, start=1):
    print(f"{no:<3} {nama["nama_barang"]:<15} Rp.{nama["harga"]:,}")

# Total harga
print(f"\nTotal: Rp.{total_harga:,}")
