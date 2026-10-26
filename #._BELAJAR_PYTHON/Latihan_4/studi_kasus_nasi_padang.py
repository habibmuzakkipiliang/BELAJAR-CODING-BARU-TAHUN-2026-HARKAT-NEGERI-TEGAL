print ("========== Selamat datang di Nasi Padang ==========")

print ("\n")

nasi = 5000
rendang = 5000
ayam = 5000
gulai_ayam = 5000
air = 5000
ati_ayam = 6000


jumlah_rendang = int (input ("Masukkan jumlah rendang = "))
jumlah_nasi = int (input ("Masukkan jumlah nasi = "))
jumlah_ayam = int (input ("Masukkan jumlah ayam = "))
jumlah_gulai_ayam = int (input ("Masukkan jumlah gulai ayam = "))
jumlah_air = int (input ("Masukkan air = "))
jumlah_ati_ayam = int (input ("Masukkan ati ayam = "))


uang_kamu = int (input ("Masukkan uang kamu : "))


jumlah_1 = jumlah_nasi * nasi
jumlah_2 = jumlah_rendang * rendang
jumlah_3 = jumlah_ayam * ayam
jumlah_4 = jumlah_ati_ayam * ati_ayam
jumlah_5 = jumlah_gulai_ayam * gulai_ayam
jumlah_6 = jumlah_air * air


total_semua = jumlah_1 + jumlah_2 + jumlah_3 + jumlah_4 + jumlah_5 + jumlah_6

kembalian = uang_kamu - total_semua

cek = uang_kamu > total_semua


out = f"""
- Total bayar   : {total_semua}
- Uang kamu     : {uang_kamu}
- Kembalian     : {kembalian}
- Cek           : {cek}
"""

print (out)

print ("\n --- batas --- \n")
