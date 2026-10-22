# Profil Habib Muzakki

print ("Profil Habib Muzakki")

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel dan Netlify"
hobi = "Ngewota JKT48"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
grup = "JKT48"
oshi = "Gracie JKT48, Aralie JKT48, Lily JKT48, Michie JKT48 dan Fritzy JKT48"
game = "Offline Style"


bio = f"""
- Nama lengkap  : {nama}
- Asal          : {asal}
- Coding        : {coding}
- Tools         : {tools}
- Hobi          : {hobi}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Grup          : {grup}
- Oshi          : {oshi}
- Game          : {game}

"""

print (bio)

print ("\n --- batas --- \n")




# Studi kasus Toko Buku Nikson

tio = """
===============================================================

Studi Kasus Toko Buku Nikson

===============================================================
"""

print (tio)


buku_tulis = 4000
buku_cerita = 5000
buku_mapel = 10000
buku_komik = 9000
canvas_lukis = 12000
pensil = 5000
penghapus = 5000
serutan = 5000
buku_paket = 10000

nama_pesan1 = str (input ("nama pemesan 1 = "))
nama_pesan2 = str (input ("nama pemesan 2 = "))
nama_pesan3 = str (input ("nama pemesan 3 = "))


jumlah_buku_tulis = int (input ("berapa buku tulis kamu = "))
jumlah_buku_cerita = int (input ("berapa buku cerita kamu = "))
jumlah_buku_komik = int (input ("berapa buku komik kamu = "))
jumlah_penghapus = int (input ("berapa penghapus kamu = "))
jumlah_pensil = int (input ("berapa pensil kamu = "))
jumlah_buku_paket = int (input ("berapa buku paket kamu = "))
jumlah_serutan = int (input ("berapa serutan kamu = "))
jumlah_canvas_lukis = int (input ("berapa canvas kamu = "))


barang = str (input ("masukkan barang kamu = "))

if barang == "pensil":
    print ("pilih")

else:
    print ("tidak dipilih")


barang1 = str (input ("masukkan barang kamu 2 = "))

if barang1 == "penghapus":
    print ("Pilih")

else:
    print ("Tidak dipilih")



barang2 = str (input ("pilih barang kamu 3 = "))

if barang2 == "serutan":
    print ("Pilih")

else:
    print ("Tidak dipilih")



barang3 = str (input ("pilih barang kamu = "))

if barang3 == "buku tulis":
    print ("Pilih")

else:
    print ("Tidak dipilih")


barang4 = str (input ("masukkan barang kamu = "))

if barang4 == "buku paket":
    print ("Pilih")

else:
    print ("Tidak dipilih")


barang5 = str (input ("barang apa yang kamu = "))

if barang5 ==  "Buku_tulis":
    print ("Pilih")

else:
    print ("Tidak dipilih")


a1 = jumlah_buku_cerita * buku_cerita 
a2 = jumlah_buku_komik * buku_komik
a3 = jumlah_buku_paket * buku_paket
a4 = jumlah_buku_tulis * buku_tulis
a5 = jumlah_canvas_lukis * canvas_lukis
a6 = jumlah_penghapus * penghapus
a7 = jumlah_pensil * pensil
a8 = jumlah_serutan * serutan

uang_kamu = int (input ("berapa uang kamu = "))


total = a1 + a2 + a3 + a4 + a5 + a6 + a6 + a7 + a8

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_pembayaran = f"""
- Nama pemesan 1    : {nama_pesan1}
- Nama pemesan 2    : {nama_pesan2}
- Nama pemesan 3    : {nama_pesan3}
- barang            : {barang}
- barang 1          : {barang1}
- barang 2          : {barang2}
- barang 3          : {barang3}
- barang 4          : {barang4}
- Total semua       : {total}
- Kembalian         : {kembalian}
- Cek               : {cek}

"""

print (rincian_pembayaran)


print ("\n --- batas ---- \n")



# Array Oshi JKT8

oshi = [
    "Gracie JKT48",
    "Aralie JKT48",
    "Lily JKT48",
    "Michie JKT48",
    "Fritzy JKT48",
]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Delyyn JKT48")
oshi.append ("Anindya JKT48")
oshi.append ("Freya JKT48")

for u in oshi:
    print (u)


print ("\n --- batas --- \n")