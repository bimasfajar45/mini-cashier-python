#Simulasi Mesin Kasir Mini

import random

total_belanja = 0
jumblah_barang = 0

hadiah_list = ["permen", "stiker", "voucher", "kurang beruntung"]

while True:
    print("\n==== input barang ====")

    # Harga random 10Rb - 100Rb
    harga = random.randrange(10000, 100001, 5000)
    print(f"Harga barang: Rp{harga}")

    total_belanja += harga
    jumblah_barang += 1

    # Kondisi diskon
    if harga >= 80000:
        diskon = 0.2
    elif harga >= 50000:
        diskon = 0.1
    else:
        diskon = 0

    potongan = harga * diskon
    harga_akhir = harga - potongan
    print(f"Diskon {diskon *100}%")
    print(f"Harga setelah diskon: Rp{harga_akhir:,}")

    #Hadiah Random
    hadiah = random.choice(hadiah_list)
    print(f"Hadiah: {hadiah}")

    # Lanjut atau tidak (loop)
    lanjut = input("Tambah barang lagi? ")
    if lanjut.lower() != "y":
        break

print('\n==== STRUK ====')
print(f"Jumblah barang {jumblah_barang}")
print(f"total belanja sebelum diskon: {total_belanja}")