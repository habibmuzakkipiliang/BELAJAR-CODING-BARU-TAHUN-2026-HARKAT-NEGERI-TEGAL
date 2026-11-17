print ("""
======================================================================================

Studi kasus tentang sistem pembayaran toko buku milik Nikson NTT Di Kota Tegal

======================================================================================

""")

buku_tulis = 9000
buku_komik = 3000
buku_majalah = 5000
buku_mapel = 6000
pensil = 3000
penghapus = 2000
serutan = 1000

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nana pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))


j_serutan = int (input ("Masukkan jumlah serutan = "))
j_pensil = int (input ("Masukkan jumlah pensil = "))
j_buku_mapel = int (input ("Masukkan jumlah buku mapel = "))
j_buku_majalah = int (input ("Masukkan jumlah buku majalah = "))
j_buku_komik = int (input ("Masukkan jumlah buku komik = "))
j_buku_tulis = int (input ("Masukkan jumlah buku tulis = "))
j_penghapus = int (input ("Masukkan jumlah penghapus = "))

a1 = j_buku_komik * buku_komik
a2 = j_buku_majalah * buku_majalah
a3 = j_buku_mapel * buku_mapel
a4 = j_pensil * pensil
a5 = j_serutan * serutan
a6 = j_penghapus * penghapus
a7 = j_buku_tulis * buku_tulis

total = a1 + a2 + a3 + a4 + a5 + a6 + a7

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_pembayaran = f"""
======================================================================================

RINCIAN PEMBAYARAN STUDI KASUS TENTANG SISTEM PEMBAYARAN TOKO BUKU MILIK NIKSON DI KOTA TEGAL

======================================================================================

- Nama pemesan 1        : {nama_pemesan1}
- Nama pemesan 2        : {nama_pemesan2}
- Nama pemesan 3        : {nama_pemesan3}
- Total                 : {total}
- Kembalian uang        : {kembalian}
- Cek                   : {cek}

"""

print (rincian_pembayaran)


print ("\n --- batas --- \n")




print ("""
=====================================================================================

STUDI KASUS TENTANG NILAI AKHIR UTS DENGAN GRADE HURUF NYA 

======================================================================================

""")


nilai = int (input ("Masukkan nilai kamu sekarang = "))

if nilai >= 95:
    print (f"Nilai A+, nilai = {nilai}")

elif nilai >= 90:
    print (f"Nilai A-, nilai = {nilai}")

elif nilai >= 85:
    print (f"Nilai B+, nilai = {nilai}")

elif nilai >= 80:
    print (f"Nilai B-, nilai = {nilai}")

elif nilai >= 70:
    print (f"Nilai C, nilai = {nilai}")

else:
    print (f"Input tidak valid")


print ("\n --- batas --- \n")