print ("Hello World")

print ("\n --- batas --- \n")



# Biodata lengkap Habib Muzakki

nama = "Habib Muzakki"
nama_panggilan = "Habib"
asal = "Kota Serang"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel dan Netlify"
marga = "Piliang"
kampus = "Universitas Harkat Negeri"
fakultas = "Sekolah Vokasi"

bio = f"""
\n - Nama lengkap       : {nama}
\n - Nama panggilan     : {nama_panggilan}
\n - Asal daerah        : {asal}
\n - Coding             : {coding}
\n - Tools              : {tools}
\n - Marga              : {marga}
\n - Kampus             : {kampus}
\n - Fakultas           : {fakultas}
"""

print (bio)

print ("\n --- batas --- \n")



# variabel dasar

greet = "Halo Dunia"
print (greet)

gun = "Halo Siang"
print (gun)

hun = "Halo anak Harkat Negeri Tegal"
print (hun)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
\n - Teks       : {teks}
\n - Angka      : {angka}
\n - Desimal    : {desimal}
\n - Cek        : {cek}
"""

print (tipe)

print ("\n --- batas --- \n")



# Cek tipe pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x * y

def pangkat (x, y):
    return x ** y

def modulus (x, y):
    return x % y


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def nama (halo):
    print (f"Halo nama saya {halo} dari Jakarta Utara")

nama ("Hayyan")
nama ("Yun")
nama ("Runer")
nama ("Rio")
nama ("Irfan")
nama ("Ivan")


print ("\n --- batas --- \n")



# Fungsi dengan parameter 2

def run (nama, asal):
    print (f"Halo nama saya {nama} dari {asal}")

run ("Hayyan", "Jakarta Utara")
run ("Rayyan", "Jakarta Timur")
run ("Hun", "Jakarta Barat")
run ("Jun", "Bandung")
run ("Kop", "Semarang")


print ("\n --- batas --- \n")



# Fungsi dasar dengan parameter 3

def run (nama, negara, daerah):
    print (f"Halo nama saya {nama} dari {negara}, dan daerah {daerah}")

run ("Hayyan", "Indonesia", "Jakarta")
run ("Nabil", "Malaysia", "Kuala Lumpur")
run ("Rafa", "Amerika Serikat", "Washington DC")
run ("Leon", "Spanyol", "Madrid")
run ("Irfan", "Jepang", "Tokyo")


print ("\n --- batas --- \n")



# Fungsi dasar

def dasar ():
    print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Oshi JKT48 (List dan Method List Python)

oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48"]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Delynn JKT48")
oshi.append ("Freya JKT48")
oshi.append ("Trisha JKT48")

for i in oshi:
    print (i)

print ("\n --- batas --- \n")



# Studi kasus tentang warung kopi sederhana milik Nikson NTT

print ("""
=============================================================================

Warung Kopi Sederhana Milik Nikson NTT

=============================================================================

""")

kopi = 4000
aqua = 3000
kentang = 5000
nasi_ayam_goreng = 3000
nasi_goreng = 6000
nasi_ayam_bakar = 7000

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 : "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 : "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 : "))

j_kopi = int (input ("Masukkan kopi = "))
j_kentang = int (input ("Masukkan kentang = "))
j_nasi_ayam_goreng = int (input ("Masukkan nasi ayam goreng = "))
j_nasi_goreng = int (input ("Masukkan nasi goreng nya = "))
j_nasi_ayam_bakar = int (input ("Masukkan nasi ayam bakar nya = "))
j_aqua = int (input ("Masukkan aqua = "))

a1 = j_aqua * aqua
a2 = j_kentang * kentang
a3 = j_kopi * kopi
a4 = j_nasi_ayam_bakar * nasi_ayam_bakar
a5 = j_nasi_goreng * nasi_goreng
a6 = j_kopi * kopi

total = a1 + a2 + a3 + a4 + a5 + a6 

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total

cek = uang_kamu > total


rincian_pembayaran = f"""
====================================================================================

RINCIAN PEMBAYARAN 

====================================================================================s

\n - Nama pemesan 1     : {nama_pemesan1}
\n - Nama pemesan 2     : {nama_pemesan2}
\n - Nama pemesan 3     : {nama_pemesan3}
\n - Uang kamu          : {uang_kamu}
\n - Total uang         : {total}
\n - Kembalian          : {kembalian}
\n - Cek                : {cek}
"""

print (rincian_pembayaran)

print ("\n --- batas --- \n")



print ("""
===================================================================================

PERCABANGAN USIA PRODUKTIF MANUSIA

===================================================================================

""")

usia = int (input ("Masukkan usia sekarang ini = "))
cek = True

if usia >= 15 and usia <= 45:
    if cek:
        print (f"Sudah masuk usia produktif manusia, usia = {usia}")

    elif usia > 45:
        print (f"Sudah tua dan harus pensiun, usia = {usia}")

else:
    print (f"Masih kecil usia nya kamu, usia = {usia}")


print ("\n --- batas --- \n")



print ("""
================================================================================

PERCABANGAN NILAI RAPOR UTS

==================================================================================
""")

nilai = int (input ("Masukkan nilai kamu sekarang = "))

if nilai >= 95:
    print (f"A+, nilai = {nilai}")

elif nilai >= 90:
    print (f"A-, nilai = {nilai}")

elif nilai >= 85:
    print (f"B+, nilai = {nilai}")

elif nilai >= 80:
    print (f"B-, nilai = {nilai}")

elif nilai >= 70:
    print (f"C, nilai = {nilai}")

elif nilai >= 60:
    print (f"D, nilai = {nilai}")

elif nilai >= 50:
    print (f"E, nilai = {nilai}")

elif nilai >= 40:
    print (f"F, nilai = {nilai}")

else:
    print (f"Input tidak valid, nilai = {nilai}")


print ("\n --- batas --- \n")
