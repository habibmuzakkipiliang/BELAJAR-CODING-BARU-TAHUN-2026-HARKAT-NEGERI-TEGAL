print ("Selamat datang di Cafe Kita")

print ("\n")

harga_es_kopi = 6000
harga_kentang = 4000
harga_nasi = 5000
harga_es_buah = 6000
harga_kopi_panas = 8000


jumlah_kopi_panas = int (input ("Masukkan jumlah kopi = "))
jumlah_kentang = int (input ("Masukkan jumlah kentang = "))
jumlah_nasi = int (input ("Masukan jumlah nasi = "))
jumlah_es_kopi = int (input ("Masukkan es Kopi = "))
jumlah_es_buah = int (input ("Masukkan es buah = "))


uang_kamu = int (input ("Masukkan uang kamu = "))


jumlah_1 = jumlah_kopi_panas * harga_kopi_panas
jumlah_2 = jumlah_kentang * harga_kentang
jumlah_3 = jumlah_nasi * harga_nasi
jumlah_4 = jumlah_es_kopi * harga_es_kopi
jumlah_5 = jumlah_es_buah * harga_es_buah

total_1 = jumlah_1 + jumlah_2 + jumlah_3 + jumlah_4 + jumlah_5

kembalian = uang_kamu - total_1

cek = kembalian > total_1



data = f"""
- Total uang    : Rp {total_1}
- Kembalian     : Rp {kembalian}
- Uang kamu     : Rp {uang_kamu}
- Cek           : {cek}
"""

print (data)


