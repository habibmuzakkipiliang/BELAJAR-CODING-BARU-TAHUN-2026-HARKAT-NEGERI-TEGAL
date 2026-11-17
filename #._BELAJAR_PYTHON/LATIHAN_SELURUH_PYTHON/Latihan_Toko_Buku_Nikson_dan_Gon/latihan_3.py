print ("Profil Habib Muzakki")

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
jurusan = "D4 Teknik Informatika"
fakultas = "Vokasi"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel, Netlify"


bio = f"""
- Nama          : {nama}
- Asal          : {asal}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Coding        : {coding}
- Tools         : {tools}
"""

print (bio)


print ("\n --- batas --- \n")


rik = f"""
========================================

TOKO BARU DAN SEJAHTERA

=======================================
"""

print (rik)

nama_pesan1 = str (input ("nama pemesan 1 = "))
nama_pesan2 = str (input ("nama pemesan 2 = "))
nama_pesan3 = str (input ("nama pemesan 3 = "))


makanan_ringan = 7000
makanan_berat = 8000
lontong = 6000
uduk = 6000
nasi = 2000
mie_instan = 2000
pop_mie = 1000
teh_manis_anget = 3000
teh_manis_es = 3000
nasi_goreng = 5000
nas_kuning = 3000

jumlah_nasi = int (input ("berapa nasi nya = "))
jumlah_teh_manis_es = int (input ("berapa teh manis es = "))
jumlah_teh_manis_anget = int (input ("berapa teh manis anget = "))
jumlah_pop_mie = int (input ("berapa pop mie nya = "))
jumlah_mie_instan = int (input ("berapa mie instan = "))
jumlah_lontong = int (input ("berapa lontong nya = "))
jumlah_uduk = int (input ("berapa uduk nya = "))
jumlah_makanan_ringan = int (input ("berapa makanan ringan nya = "))
jumlah_makanan_berat = int (input ("berapa makanan berat nya = "))
jumlah_nasi_goreng = int (input ("berapa nasi goreng nya = "))
jumlah_nasi_kuning = int (input ("berapa nasi kuning nya = "))

a1 = jumlah_lontong * lontong
a2 = jumlah_makanan_berat * makanan_berat
a3 = jumlah_makanan_ringan * makanan_ringan
a4 = jumlah_nasi * nasi
a5 = jumlah_mie_instan * mie_instan
a6 = jumlah_pop_mie * pop_mie
a7 = jumlah_uduk * uduk
a8 = jumlah_teh_manis_es * teh_manis_es 
a9 = jumlah_teh_manis_anget * teh_manis_anget
a10 = jumlah_nasi_goreng * nasi_goreng 
a11 = jumlah_nasi_kuning * nas_kuning

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11

uang_kamu = int (input ("berapa uang kamu nya = "))

kembalian = uang_kamu - total

cek = kembalian > total

rincian_pembayaran = f"""
- Total semua       : {total}
- Kembalian         : {kembalian}
- Cek               : {cek}

"""
print (rincian_pembayaran)

print ("\n --- batas --- \n")



