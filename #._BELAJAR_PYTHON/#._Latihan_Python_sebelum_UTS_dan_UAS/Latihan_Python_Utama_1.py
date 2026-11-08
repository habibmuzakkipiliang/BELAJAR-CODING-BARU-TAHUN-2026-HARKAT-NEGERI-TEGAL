# Hello World

print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

greet = "Halo JKT48"
feer = "Halo Pagi hari"

print (greet)
print (feer)

print ("\n --- batas --- \n")



# variabel dasar + Tipe data pemrograman

a = "Halo Dunia"
b = 12
c = 12.12
d = True

den = f"""
- A : {a}
- B : {b}
- C : {c}
- D : {d}

"""

print (den)


print ("\n --- batas --- \n")





# Cek tipe pemrograman

print ("A :", type (a))
print ("B :", type (b))
print ("C :", type (c))
print ("D :", type (d))


print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

x = int (input ("Masukkan angka x : "))
y = int (input ("Masukkan angka y : "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x ** y

def bagi (x, y):
    return x / y

def pangkat (x, y):
    return x ** y

def modulus (x, y):
    return x % y


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Bagi =", bagi (x, y))
print ("Modulus =", modulus (x, y))
print ("Pangkat =", pangkat (x, y))


print ("\n --- batas --- \n")





print ("""
======================================================================================

RUMUS-RUMUS BANGUN DATAR SEDERHANA

======================================================================================

""")


# Luas persegi

s = int (input ("Masukkan sisi = "))

def persegi (s):
    return s * s

print ("Luas persegi =", persegi (s, s))

print ("\n --- batas --- \n")


# Luas Persegi Panjang

p = int (input ("Masukkan panjang persegi = "))
l = int (input ("Masukka lebar persegi = "))

def persegi_panjang (p, l):
    return p * l

print ("Luas persegi panjang =", persegi_panjang (p, l))


print ("\n --- batas --- \n")


# Segitiga

a = int (input ("Masukkan alas segitiga = "))
t = int (input ("Masukkan tinggi segitiga = "))

def segitiga (a, t):
    return a * t / 2

print ("Luas segitiga =", segitiga (a, t))


print ("\n --- batas --- \n")



# Lingkaran

phi = 3.14
r = int (input ("Masukkan r = "))

def lingkaran (phi, r):
    return phi * r * r

print ("Luas lingkaran =", lingkaran (phi, r))


print ("\n --- batas --- \n")



print ("""
======================================================================================

STUDI KASUS TENTANG KOPI BAHAGIA MILIK JOJO

=====================================================================================

""")

kopi = 5000
kentang = 6000
aqua = 2000
nasi_ayam_goreng = 5000
nasi_ayam_bakar = 6000
nasi_ayam_geprek = 6000
nasi_goreng = 4000
mie_ayam = 5000

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 : "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 : "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 : "))


j_mie_ayam = int (input ("Masukkan mie ayam = "))
j_nasi_goreng = int (input ("Masukkan nasi goreng = "))
j_nasi_ayam_geprek = int (input ("Masukkan nasi ayam geprek = "))
j_nasi_ayam_bakar = int (input ("Masukkan nasi ayam bakar = "))
j_nasi_ayam_goreng = int (input ("Masukkan nasi ayam goreng = "))
j_aqua = int (input ("Masukkan aqua nya = "))
j_kentang = int (input ("Masukkan kentang = "))
j_kopi = int (input ("Masukkan kopi = "))


a1 = j_aqua * aqua
a2 = j_kentang * kentang
a3 = j_kopi * kopi
a4 = j_nasi_ayam_bakar * nasi_ayam_bakar
a5 = j_mie_ayam * mie_ayam
a6 = j_nasi_ayam_goreng * nasi_ayam_goreng
a7 = j_kopi * kopi
a8 = j_nasi_ayam_geprek * nasi_ayam_geprek


total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

uang_kamu = int (input ("masukkan uang kamu sekarang ini = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_biaya = f"""
\n - Nama pemesan 1     : {nama_pemesan1}
\n - Nama pemesan 2     : {nama_pemesan2}
\n - Nama pemesan 3     : {nama_pemesan3}
\n - Total uang         : {total}
\n - Kembalian          : {kembalian}
\n - Cek                : {cek}



"""

print (rincian_biaya)

print ("\n --- batas --- \n")




print ("""
=====================================================================================

STUDI KASUS PERCABANGAN CUACA SEKARANG 

==========================================


""")

cuaca = str (input ("Masukkan cuaca sekarang ya (cerah, berawan, hujan) : " ))
suhu = int (input ("Masukkan suhu sekarang dalam celcius : "))
cek = True

if cuaca == "cerah":
    if cek:
        if suhu > 30:
            print (f"Boleh keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

        else:
            print (f"Bawa topi kalau keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"Boleh keluar rumah, sambil olahraga, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Gak boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Jangan keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"Harus pakai payung saat hujan turun, suhu = {suhu} dan cuaca = {cuaca}")


else:
    print (f"Input tidak valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")




print ("""
====================================================================================

PERCABANGAN USIA PRODUKTIF MANUSIA 

===================================================================================

""")

usia = int (input ("Masukkan usia sekarang ini :  "))
cek = True

if usia >= 15 and usia <= 45:
    if cek:
        print (f"Sudah masuk usia produktif, usia = {usia}")

    elif usia > 45:
        print (f"Sudah tua, usia = {usia}")

else:
    print (f"Masih kecil usianya, usia = {usia}")


print ("\n --- batas --- \n")



print ("""
=====================================================================================

PERCABANGAN USIA JOIN KERJA 

======================================================================================

""")

usia = int (input ("Masukkan usia kamu saat ini : "))
cek = True

if usia >= 25 and usia <= 45:
    if cek:
        print (f"Sudah boleh kerja, usia = {usia}")

    elif usia > 45:
        print (f"Sudah tua usia saat ini, usia = {usia}")

else:
    print (f"Masih belum produktif usia nya, usia = {usia}")


print ("\n --- batas --- \n")




print ("""
===================================================================================

USIA MASUK DAN GABUNG KE JKT48 DAN

===================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if usia >= 13 and usia <= 19:
    if cek:
        print (f"Sudah cukup untuk daftar dan join JKT48, usia = {usia}")

    elif usia > 19:
        print (f"Sudah boleh gabung, usia = {usia}")

else:
    print (f"Masih kecil usia nya, usia = {usia}")


print ("\n --- batas --- \n")



print ("""
======================================================================================

DAFTAR OSHI-OSHI JKT48

======================================================================================
""")

oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48"]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Delynn JKT48")
oshi.append ("Freya JKT48")

for i in oshi:
    print (i)

print ("\n --- batas --- \n")



print ("""
====================================================================================

DICTIONARY 

======================================================================================
""")

data = {
    "nama" : "Habib Muzakki",
    "kelas" : "1b",
    "asal_daerah" : "Kota Serang",
    "coding" : "HTML, CSS, JavaScript dan Python",
    "tools" : "Github, Github Pages, Vercel dan Netlify",
}

print ("Nama :", data ["nama"])
print ("Kelas :", data ["kelas"])
print ("Asal :", data ["asal_daerah"])
print ("Coding :", data ["coding"])
print ("Tools :", data ["tools"])


print ("\n --- batas --- \n")