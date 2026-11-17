# Studi kasus toko alfamart

print ("Studi kasus toko alfamart")


nama = "Habib Muzakki"
kelas = "1B"
asal = "Kota Serang, Banten"
matkul = "Pengantar Pemrograman"

jn = f"""
- Nama lengkap  : {nama}
- Kelas         : {kelas}
- Asal          : {asal}
- Matkul        : {matkul}

"""

print (jn)

print ("\n --- batas --- \n")



# switch case 

a = 9 

match (a):

    case 1:
        print (1)

    case 2:
        print (2)

    case 3:
        print (3)

    case _:
        print ("Semula")


print ("\n --- batas --- \n")


# Daftar barang-barang di Alfamart

roti = 9000
air = 4000
makanan_ringan = 3000
nasi = 6000
ayam_geprek = 4000
ayam_goreng = 6000

jumlah_air = int (input ("Masukkan jumlah air = "))
jumlah_nasi = int (input ("Masukkan jumlah nasi = "))
jumlah_ayam_geprek = int (input ("Masukkan ayam geprek = "))
jumlah_ayam_goreng = int (input ("Masukkan ayam goreng = "))
jumlah_roti = int (input ("Masukkan jumlah roti = "))

a1 = jumlah_air * air
a2 = jumlah_ayam_geprek * ayam_geprek
a3 = jumlah_nasi * nasi 
a4 = jumlah_roti * roti

total = a1 + a2 + a3 + a4 

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = total - uang_kamu

cek = total > kembalian

rincian = f"""
- Total         : {total}
- Kembalian     : {kembalian}
- Cek           : {cek}

"""

print (rincian)

