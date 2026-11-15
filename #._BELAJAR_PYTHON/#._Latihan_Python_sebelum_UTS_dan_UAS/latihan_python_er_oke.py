print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar 

a = "Halo Dunia"
print (a)

b = "Halo Skyline"
print (b)

c = 12
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo Dunia saya yang sangat indah"
angka = 12
desimal = 44.3
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}

"""

print (cek)

print ("\n --- batas --- \n")



# Cek tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi return dengan operator dasar

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

def bagi (x, y):
    return x / y

def modulus (x, y):
    return x % y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terbesar

def angka_besar (r, t):

    if r > t:
        return r 

    else:
        return t

print ("Angka besar =", angka_besar (10, 5))
print ("Angka besar =", angka_besar (4, 23))
print ("Angka besar =", angka_besar (5, 90))
print ("Angka besar =", angka_besar (4, 23))
print ("Angka besar =", angka_besar (5, 60))
print ("Angka besar =", angka_besar (4, 50))


print ("\n --- batas --- \n")



# Fungsi return dengan mencari angka terkecil

def angka_kecil (a, b):

    if a < b:
        return a 

    else:
        return b

print ("Angka kecil =", angka_kecil (1, 20))
print ("Angka kecil =", angka_kecil (4, 23))
print ("Angka kecil =", angka_kecil (50, 4))
print ("Angka kecil =", angka_kecil (4, 50))
print ("Angka kecil =", angka_kecil (4, 56))
print ("Angka kecil =", angka_kecil (540, 47))


print ("\n --- batas --- \n")




# Studi kasus tentang cafe bahagia milik Nikson NTT

print ("""
=======================================================

Studi kasus tentang cafe bahagia milik Nikson NTT

======================================================

""")

kopi = 4000
aqua = 3000
kentang = 4000
nasi_goreng = 6000
mie_goreng = 7000
mie_ayam = 4000
bakso = 5000

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))


j_bakso = int (input ("Masukkan bakso nya = "))
j_kopi = int (input ("Masukkan kopi nya = "))
j_kentang = int (input ("Masukkan kentang nya = "))
j_nasi_goreng = int (input ("Masukkan nasi goreng nya = "))
j_mie_goreng = int (input ("Masukkan mie goreng nya = "))
j_mie_ayam = int (input ("Masukkan mie ayam nya = "))
j_bakso = int (input ("Masukkan bakso nya = "))


a1 = j_bakso * bakso
a2 = j_kopi * kopi
a3 = j_kentang * kentang
a4 = j_mie_ayam * mie_ayam
a5 = j_nasi_goreng * nasi_goreng
a6 = j_mie_ayam * mie_ayam
a7 = j_nasi_goreng * nasi_goreng

total = a1 + a2 + a3 + a4 + a5 + a6 + a7

uang_kamu = int (input ("Masukkan uang kamu sekarang ini = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_pembayaran = f"""
============================================

RINCIAN PEMBAYARAN CAFE BAHAGIA MILIK NIKSON NTT

=============================================

\n Nama pemesan 1   : {nama_pemesan1}
\n Nama pemesan 2   : {nama_pemesan2}
\n Nama pemesan 3   : {nama_pemesan3}
\n Total uang       : {total}
\n Kembalian uang   : {kembalian}
\n Cek uang         : {cek}
"""

print (rincian_pembayaran)


print ("\n --- batas --- \n")



# Studi kasus mencari nilai 

nilai = int (input ("Masukkan nilai kamu sekarang ini = "))

if nilai >= 90:
    print (f"Nilai kamu A, nilai = {nilai}")

elif nilai >= 80:
    print (f"Nilai kamu B, nilai = {nilai}")

elif nilai >= 70:
    print (f"Nilai kamu C, nilai = {nilai}")

elif nilai >= 60:
    print (f"Nilai kamu D, nilai = {nilai}")

elif nilai >= 50:
    print (f"Nilai kamu E, nilai = {nilai}")

elif nilai >= 40:
    print (f"Nilai kamu F, nilai = {nilai}")

else:
    print (f"Input tidak valid, nilai = {nilai}")


print ("\n --- batas --- \n")



# Studi kasus tentang percabangan usia produktif manusia 

usia = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if usia >= 15 and usia <= 40:
    if cek:
        print (f"Usia kamu sudah produktif, usia = {usia}")

    elif usia > 40:
        print (f"Sudah tua, usia = {usia}")

else:
    print (f"Masih belum produktif, usia = {usia}")


print ("\n --- batas --- \n")




# Studi kasus tentang Percabangan daftar dan join JKT48

usia_kamu = int (input ("Masukkan usia kamu sekarang ini = "))
jenjang = str (input ("Masukkan jenjang pendidikan kamu = "))
cek = True

if jenjang == "sd":
    if usia_kamu >= 13 and usia_kamu <= 20:
        if cek:
            print (f"Boleh masuk dan daftar JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

        else:
            print (f"Jangan masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

elif jenjang == "smp":
    if usia_kamu >= 13 and usia_kamu <= 20:
        print (f"Boleh masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

    else:
        print (f"Jangan masuk dulu ya")

elif jenjang == "sma":
    if usia >= 13 and usia_kamu <= 20:
        print (f"Boleh masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

    else:
        print (f"Jangan masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

elif jenjang == "kuliah":
    if usia >= 13 and usia <= 20:
        print (f"Sudah boleh masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

    else:
        print (f"Jangan masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

elif usia > 20:
    print (f"Boleh masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")

else:
    print (f"Belum boleh masuk JKT48, usia = {usia_kamu} dan jenjang = {jenjang}")


print ("\n --- batas --- \n")