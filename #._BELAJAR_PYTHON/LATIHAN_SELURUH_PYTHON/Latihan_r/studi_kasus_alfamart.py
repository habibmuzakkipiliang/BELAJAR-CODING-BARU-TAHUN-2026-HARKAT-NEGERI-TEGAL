# Hello World

print ("Hello World")


print ("Selamat datang di Alfamart")


fr = "Pemilik oleh Habib Muzakki, D4 Teknik Informatika"
print (fr)


air_minum_500ml = 3000
air_minum_1500ml = 5000
air_teh_manis = 2000
ayam_geprek = 5000
ayam_goreng = 6000
nasi = 4000 
nasi_goreng = 5000
cemilan_ringan = 4000
kopi = 3000
kentang = 2000


jumlah_kentang = int (input ("Masukkan jumlah kentang = "))
jumlah_kopi = int (input ("Masukkan jumlah kopi = "))
jumlah_cemilan_ringan = int (input ("Masukkan jumlah cemilan ringan = "))
jumlah_nasi_goreng = int (input ("Masukkan jumlah nasi goreng = "))
jumlah_ayam_goreng = int (input ("Masukkan jumlah ayam goreng = "))
jumlah_ayam_geprek = int (input ("Masukkan jumlah ayam geprek = "))
jumlah_air_teh_manis = int (input ("Masukkan jumlah air teh manis = "))
jumlah_minum_500ml = int (input ("Masukkan jumlah minum 500 ml ="))
jumlah_minum_1500ml = int (input ("Masukkan jumlah minum 1500 ml = "))


uang_kamu = int (input ("Masukkan uang kamu = "))

b1 = jumlah_air_teh_manis * air_teh_manis
b2 = jumlah_nasi_goreng * nasi_goreng
b3 = jumlah_minum_500ml * air_minum_500ml
b4 = jumlah_minum_1500ml * air_minum_1500ml
b5 = jumlah_kentang * kentang
b6 = jumlah_kopi * kopi
b7 = jumlah_ayam_geprek * ayam_geprek 
b8 = jumlah_ayam_goreng * ayam_goreng

total = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8

kembalian = total - uang_kamu

cek = total > uang_kamu

infor = f"""
- Total semua   : {total}
- Kembalian     : {kembalian}
- Cek           : {cek}


"""

print (infor)
