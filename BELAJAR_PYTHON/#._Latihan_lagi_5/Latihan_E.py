print ("Hello World")

print ("Selamat datang di Proyek Saya")

nama = "Habib Muzakki"
kelas = "1B"
asal = "Kota Serang, Banten"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel dan Netlify"
hobi = "JKT48 dan Ngewota Gracie JKT48"


bio = f"""
- Nama lengkap  : {nama}
- Asal          : {asal}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Coding        : {coding}
- Tools         : {tools}
- Hobi          : {hobi}
"""

print (bio)


print ("\n --- batas --- \n")





# latihan Studi Kasus Python

ri = """
===============================

LATIHAN STUDI KASUS PYTHON

===================================
"""

print (ri)


nasi_goreng = 9000
nasi_kuning = 7000
nasi_campur = 5000
nasi_lengko = 5000
teh_manis_anget = 2000
teh_manis_es = 1000
air_minum = 1000


# jumlah dan harga 

jumlah_nasi_goreng = int (input ("berapa porsi nasi goreng = "))
jumlah_nasi_kuning = int (input ("berapa porsi nasi kuning = "))
jumlah_nasi_campur = int (input ("berapa porsi nasi campur = "))
jumlah_teh_manis_anget = int (input ("berapa teh manis anget = "))
jumlah_teh_manis_es = int (input ("berapa teh manis es = "))
jumlah_nasi_lengko = int (input ("berapa porsi nasi lengko = "))
jumlah_air_minum = int (input ("berapa air minum = "))


a1 = jumlah_air_minum * air_minum
a2 = jumlah_nasi_campur * nasi_campur
a3 = jumlah_nasi_goreng * nasi_goreng
a4 = jumlah_nasi_lengko * nasi_lengko
a5 = jumlah_teh_manis_anget * teh_manis_anget
a6 = jumlah_teh_manis_es * teh_manis_es

uang_kamu = int (input ("berapa uang kamu = "))

total = a1 + a2 + a3 + a4 + a5 + a6

kembalian = uang_kamu - total

cek = uang_kamu > total


barang1 = str (input ("masukkan barang kamu = "))

if barang1 == "ada barang":
    print ("Ada")

elif barang1 == "baru kirim":
    print ("kirim")

else:
    print ("hilang")


print ("\n --- batas --- \n")



barang2 = str (input ("masukkan barang 2 kamu = "))

if barang2 == "ada_barangnya":
    print ("Ada barangnya")

elif barang2 == "lagi dikirim":
    print ("lagi dikirim")

else:
    print ("hilang")


print ("\n --- batas --- \n")


oshi = [
    "Gracie JKT48",
    "Aralie JKT48",
    "Lily JKT48",
    "Fritzy JKT48",
    "Michie JKT48",
]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Freya JKT48")
oshi.append ("Anindya JKT48")
oshi.append ("Olla JKT48")

for i in oshi:
    print (i)


print ("\n --- batas --- \n")


rincian_pembayaran = f"""
- Total semua       : {total}
- Kembalian         : {kembalian}
- Cek               : {cek}

"""
print (rincian_pembayaran)

print ("\n --- batas ---- \n")
