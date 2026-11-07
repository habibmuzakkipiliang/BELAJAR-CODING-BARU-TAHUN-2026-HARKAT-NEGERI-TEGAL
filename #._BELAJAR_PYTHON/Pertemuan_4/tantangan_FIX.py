print("Selamat datang di Warung Kopi Ceria")


harga_kopi = 15000
harga_sandwich = 25000
harga_kentang = 20000


harga_asli = f"""

================= Daftar Harga ===================

- Kopi      : Rp. {harga_kopi}/Gelas
- Sandwich  : Rp. {harga_sandwich}/porsi
- Kentang   : Rp. {harga_kentang}/porsi

"""

print(harga_asli)


jumlah_kopi = int(input("Masukkan jumlah kopi = "))
jumlah_sandwich = int(input("Masukkan jumlah sandwich = "))
jumlah_kentang = int(input("Masukkan jumlah kentang = "))
uang_bayar = int(input("Masukkan uang bayar = "))


jumlah_harga_1 = harga_kopi * jumlah_kopi
jumlah_harga_2 = harga_kentang * jumlah_kentang
jumlah_harga_3 = harga_sandwich * jumlah_sandwich

total_harga = jumlah_harga_1 + jumlah_harga_2 + jumlah_harga_3

kembalian = uang_bayar - total_harga

rincian = f"""

================= RINCIAN PEMBELIAN ===================

Kopi      : {jumlah_kopi}
Sandwich  : {jumlah_sandwich}
Kentang   : {jumlah_kentang}

=========================================================

Total harga              : Rp. {total_harga}
Uang yang dibayarkan     : Rp. {uang_bayar}
Kembalian mu             : Rp. {kembalian}
"""

print(rincian)