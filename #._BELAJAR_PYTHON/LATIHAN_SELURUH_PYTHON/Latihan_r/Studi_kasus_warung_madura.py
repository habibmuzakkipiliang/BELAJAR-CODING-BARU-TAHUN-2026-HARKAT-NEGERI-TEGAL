print ("Studi Kasus Warung Madura")


nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
kelas = "1B"
golongan_darah = "B"
fakultas = "Vokasi"
jurusan = "D4 Teknik Informatika" 

fn = f"""
- Nama lengkap  : {nama}
- Asal          : {asal}
- Kelas         : {kelas}
- Gol darah     : {golongan_darah}
- Fakultas      : {fakultas}
- Jurusan       : {jurusan}
- 

"""

print (fn)

print ("\n --- batas --- \n")



print ("Daftar menu dibawah ini")

makanan_ringan = 3000
makanan_berat = 9000
minum_1500ml = 6000
minum_500ml = 5000

jumlah_makanan_ringan = int (input ("Masukkan jumlah makanan ringan = "))
jumlah_makanan_berat = int (input ("Masukkan jumlah makanan berat = "))
jumlah_minum_1500ml = int (input ("Masukkan jumlah minum 1500 ml = "))
jumlah_minum_500ml = int (input ("Masukkkan jumlah minum 500 ml = "))


uang_kamu = int (input ("Masukkan uang kamu = "))


a1 = jumlah_makanan_berat * makanan_berat
a2 = jumlah_makanan_ringan * makanan_ringan
a3 = jumlah_minum_1500ml * minum_1500ml
a4 = jumlah_minum_500ml * minum_500ml

total = a1 + a2 + a3 + a4

kembalian = total - uang_kamu

cek = total > kembalian


info = f"""
- Total     : {total}
- Kembalian : {kembalian}
- Cek       : {cek}
"""

print (info)

print ("\n --- batas --- \n")


