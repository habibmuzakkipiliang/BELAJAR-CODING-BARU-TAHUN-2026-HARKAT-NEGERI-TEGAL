frin = """
===================================================================

\n TOKO BUKU DAN ALAT TULIS MILIK NIKSON, GOGON DAN BOGE NTT

===================================================================

"""

print (frin)


buku_tulis = 5000
buku_jurnal = 6000
buku_cerita = 7000
buku_komik = 6000
buku_nota = 9000
pensil = 2000
penghapus = 2000
serutan = 4000
pulpel = 2000
tipe_x = 4000


jumlah_buku_tulis = int (input ("Pesen buku tulis berapa = "))
jumlah_buku_cerita = int (input ("Pesen buku cerita berapa = "))
jumlah_buku_komik = int (input ("Pesen buku komik berapa = "))
jumlah_buku_jurnal = int (input ("Pesen buku jurnal berapa = "))
jumlah_buku_nota = int (input ("Pesen buku nota berapa = "))
jumlah_pensil = int (input ("Pesen pensil berapa = "))
jumlah_penghapus = int (input ("Pesen penghapus berapa = "))
jumlah_pulpen = int (input ("Pesen pulpen berapa = "))
jumlah_tipe_x = int (input ("Pesen tipe x berapa = "))


a1 = jumlah_pensil * pensil
a2 = jumlah_buku_tulis * buku_tulis
a3 = jumlah_buku_cerita * buku_cerita
a4 = jumlah_pulpen * pulpel
a5 = jumlah_buku_jurnal * buku_jurnal
a6 = jumlah_penghapus * penghapus
a7 = jumlah_pulpen * pulpel
a8 = jumlah_tipe_x * tipe_x

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

uang_kamu = int (input ("Uang kamu ada berapa = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_pembayaran = f"""

- Total     : {total}
- Kembalian : {kembalian}
- Cek       : {cek}

"""

print (rincian_pembayaran)