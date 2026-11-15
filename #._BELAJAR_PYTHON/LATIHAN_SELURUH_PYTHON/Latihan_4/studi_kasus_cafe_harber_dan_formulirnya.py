print ("Selamat datang di Cafe Harber \n")


print ("Formulir kamu isi dong \n")

nama = input ("Masukkan nama kamu = ")
asal = input ("Masukkan asal daerah kamu = ")
jurusan = input ("Masukkan jurusan kamu = ")
fakultas = input ("Masukkan fakultas kamu = ")
nim = int (input ("Masukkan nim kamu = "))

profil = f"""
- Nama lengkap      : {nama}
- Asal              : {asal}
- Jurusan           : {jurusan}
- Fakultas          : {fakultas}
- NIM               : {nim}
"""

print (profil)


print ("\n --- batas --- \n")



# Daftar menu lengkap
 
kopi_kapalapi = 5000
kopi_cappucino = 7000
kopi_luwak = 8000
kopi_hitam = 10000
kentang = 5000
nasi = 3000
minum = 1000

jumlah_kopi_hitam = int (input ("Masukkan jumlah kopi hitam = "))
jumlah_kopi_luwak = int (input ("Masukkan jumlah kopi luwak = "))
jumlah_kopi_kapalapi = int (input ("Masukkan kopi kapalapi = "))
jumlah_kentang = int (input ("Masukkan jumlah kentang = "))
jumlah_cappucino = int (input ("Masukkan cappucino = "))
jumlah_nasi = int (input ("Masukkan jumlah nasi = "))
jumlah_minum = int (input ("Masukkan minum = "))

uang_kamu = int (input ("Masukkan uang kamu = "))

t_1 = kentang * jumlah_kentang 
t_2 = nasi * jumlah_nasi
t_3 = minum * jumlah_minum
t_4 = kopi_hitam * jumlah_kopi_hitam
t_5 = kopi_cappucino * jumlah_cappucino
t_6 = kopi_kapalapi * jumlah_kopi_kapalapi

jumlah = t_1 + t_2 + t_3 + t_4 + t_5 + t_6

kembalian = jumlah - uang_kamu

cek = kembalian < jumlah

data = f"""
- Total bayar   : {jumlah}
- Kembalian     : {kembalian}
- cek           : {cek}

"""

print (data)


print ("\n --- batas --- \n")

