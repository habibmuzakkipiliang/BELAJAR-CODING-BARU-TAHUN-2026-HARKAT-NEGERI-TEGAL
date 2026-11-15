print ("Profi Habib Muzakki")

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
jurusan = "D4 Teknik Informatika"
fakultas = "Vokasi"
coding = "HTML, CSS, JavaScript dan Python"


bio = f"""
- Nama      : {nama}
- Asal      : {asal}
- Jurusa    : {jurusan}
- Fakultas  : {fakultas}
- Coding    : {coding}


"""

print (bio)


print ("\n --- batas --- \n")



judul = f"""
==================================================

\t\t TOKO BUKU NIKSON NTT \t\t 

===================================================

"""

print (judul)


buku_tulis = 3000
buku_paket_mapel = 6000
pensil = 6000
penghapus = 3000
serutan = 2000


jumlah_buku_tulis = int (input ("Pesen buku tulis berapa = "))
jumlah_pensil = int (input ("Pesen pensil berapa = "))
jumlah_penghapus = int (input ("Pesen penghapus berapa = "))
jumlah_serutan = int (input ("Pesen serutan berapa = "))


a1 = jumlah_buku_tulis * buku_tulis
a2 = jumlah_pensil * pensil
a3 = jumlah_penghapus * penghapus
a4 = jumlah_serutan * serutan


total = a1 + a2 + a3 + a4


uang_kamu = int (input ("Uang kamu ada berapa = "))


kembalian = total - uang_kamu

cek = total > uang_kamu


rincian = f"""
- Total     : {total}
- Kembalian : {kembalian}
- Cek       : {cek}

"""

print (rincian)


print ("\n --- batas --- \n")