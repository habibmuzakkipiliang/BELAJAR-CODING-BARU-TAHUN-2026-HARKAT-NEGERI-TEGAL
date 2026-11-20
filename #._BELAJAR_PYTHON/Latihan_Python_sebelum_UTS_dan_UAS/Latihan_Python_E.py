print ("Hello World")


print ("\n --- batas --- \n")



# Variabel dasar

a = "Halo pagi hari"
print (a)

b = "Halo saya Habib Muzakki Dari D4 Teknik Informatika"
print (b)

c = "Halo Harkat Negeri"
print (c)

d = "Halo Gracie JKT48 yang cantik dan imut"
print (d)

e = "Halo Aralie JKT48 yang cantik dan imut"
print (e)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True


tipe = f"""
\n Teks         : {teks}
\n Angka        : {angka}
\n Desimal      : {desimal}
\n Cek          : {cek}

"""

print (tipe)

print ("\n --- batas --- \n")




# Cek tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi return dengan operator dasar

a = int (input ("Masukkan angka a = "))
b = int (input ("Masukkan angka b = "))

def tambah (a, b):
    return a + b

def kurang (a, b):
    return a - b

def kali (a, b):
    return a * b

def pangkat (a, b):
    return a ** b

def bagi (a, b):
    return a / b

def modulus (a, b):
    return a % b

print ("Tambah =", tambah (a, b))
print ("Kurang =", kurang (a, b))
print ("Kali =", kali (a, b))
print ("Pangkat =", pangkat (a, b))
print ("Bagi =", bagi (a, b))
print ("Modulus =", modulus (a, b))


print ("\n --- batas --- \n")



# Studi kasus tentang penjualan tiket JKT48

print ("""
====================================================

Studi kasus tentang penjualan tiket JKT48

===================================================
""")

j_harga_tiket_parkir = int (input ("Masukkan tiket parkir kamu sekarang (dalam rp) = "))
j_meet_and_greet = int (input ("Masukkan tiket meet and greet = "))
j_two_shoot_with_member = int (input ("Masukkan tiket two shoot with member = "))
j_theater_fx = int (input ("Masukkan tiket theater FX Sudirman = "))
j_handshake = int (input ("Masukkan tiket handshake = "))
usia = int (input ("Masukkan usia kamu sekarang = "))
harga_tiket_parkir = 50000
handshake = 50000
meet_and_greet = 60000
two_shoot_with_member = 70000
theater_fx = 60000


nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))


a1 = j_harga_tiket_parkir * harga_tiket_parkir
a2 = j_meet_and_greet * meet_and_greet
a3 = j_handshake * handshake
a4 = j_theater_fx * theater_fx
a5 = j_two_shoot_with_member * two_shoot_with_member

total_uang = a1 + a2 + a3 + a4 + a5

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian_uang = uang_kamu - total_uang

cek = uang_kamu > total_uang

rincian_pembayaran = f"""
===============================================

RINCIAN PEMBAYARAN DETAIL TIKET JKT48

===============================================

\n Nama pemesan 1       : {nama_pemesan1}
\n Nama pemesan 2       : {nama_pemesan2}
\n Nama pemesan 3       : {nama_pemesan3}
\n Total uang kamu      : {total_uang}
\n Uang kamu sekarang   : {uang_kamu}
\n Kembalian uang       : {kembalian_uang}
\n Cek kembalian        : {cek}
\n Usia kamu            : {usia}

"""

print (rincian_pembayaran)

if usia >= 13 and usia <= 19:
    print (f"Sudah boleh masuk Theater JKT48, usia = {usia}")

elif usia > 19:
    print (f"Sudah lebih dari cukup, usia kamu = {usia}")

else:
    print (f"Masih kecil usia kamu, butuh orang dewasa, usia kamu = {usia}")

print ("\n --- batas --- \n")



