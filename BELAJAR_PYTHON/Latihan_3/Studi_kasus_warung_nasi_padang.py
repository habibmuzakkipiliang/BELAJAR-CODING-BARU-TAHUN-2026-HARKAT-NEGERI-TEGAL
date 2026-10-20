print ("Selamat datang di Warung Nasi Padang Habib Muzakki")

harga_rendang = 4000
harga_nasi = 5000
harga_minum_air = 6000
harga_kuah_kacang = 8000
harga_ayam_pop = 4000
harga_ayam_gulai = 7000


jumlah_ayam_gulai = int (input ("Masukkan jumlah gulai ayam = "))
jumlah_kuah_kacang = int (input ("Masukkan kuah kacang = "))
jumlah_ayam_pop = int (input ("Masukkan ayam pop = "))
jumlah_rendang = int (input ("Masukkan ayam rendang = "))
jumlah_minum_air = int (input ("Masukkan minum air = "))
jumlah_nasi = int (input ("Masukkan jumlah nasi = "))


uang_kamu = int (input ("Masukkkan uang kamu = "))



t_1 = jumlah_ayam_gulai * harga_ayam_gulai
t_2 = jumlah_nasi * harga_nasi
t_3 = jumlah_rendang * harga_rendang
t_4 = jumlah_kuah_kacang * harga_kuah_kacang
t_5 = jumlah_ayam_pop * harga_ayam_pop

total = t_1 + t_2 + t_3 + t_4 + t_5

kembalian = total - uang_kamu

cek = kembalian < total


info = f"""
- Total     : {total}
- Kembalian : {kembalian}
- Cek       : {cek}


"""

print (info)


print ("\n --- batas --- \n")




print ("Selamat datang di Warung Kopi Habib Muzakki")

kopi = 8000
air = 2000
nasi = 3000
kentang = 5000
agar_agar = 6000


jumlah_kopi = int (input ("Masukkan jumlah kopi sekarang = "))
jumlah_kentang = int (input ("Masukkan jumlah kentang = "))
jumlah_agar_agar = int (input ("Masukkan jumlah agar-agar = "))
jumlah_air = int (input ("Masukkan jumlah air = "))


r_1 = jumlah_kopi * kopi
r_2 = jumlah_kentang * kentang
r_3 = jumlah_agar_agar * agar_agar
r_4 = jumlah_air * air

total = r_1 + r_2 + r_3 + r_4 


uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = total - uang_kamu


fio = f"""
- Total uang kamu   : {total}
- Uang kamu         : {uang_kamu}
- Kembalian         : {kembalian}

"""

print (fio)


print ("\n --- batas --- \n")