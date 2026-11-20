# Variabel dasar

a = "Halo Dunia"
print (a)

b = 12
print (b)

c = 12.12
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 12.2
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}

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

def bagi (x, y):
    return x / y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Bagi =", bagi (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")


# Fungsi return dengan mencari angka terbesar

def besar (a, b):

    if a > b:
        return a

    else:
        return b

print ("Angka besar =", besar (10, 3))
print ("Angka besar =", besar (40, 5))
print ("Angka besar =", besar (56, 34))
print ("Angka besar =", besar (34, 3))
print ("Angka besar =", besar (34, 23))
print ("Angka besar =", besar (45, 22))


print ("\n --- batas --- \n")




# Fungsi return dengan mencari angka terkecil

def kecil (f, g):

    if f < g:
        return f

    else:
        return g

print ("Angka kecil =", kecil (3, 23))
print ("Angka kecil =", kecil (4, 40))
print ("Angka kecil =", kecil (45, 2))
print ("Angka kecil =", kecil (45, 7))
print ("Angka kecil =", kecil (9, 340))


print ("\n --- batas --- \n")



angka_random = int (input ("Masukkan angka random dari 1 - 20 = "))

if angka_random >= 1 and angka_random <= 20:
    print ("Termasuk angka random yang tepat",)

elif angka_random >= 20:
    print ("Lebih dari 20")

elif angka_random <= 1:
    print ("Gak valid")

else:
    print ("Selamat anda selesai")
    print ("Jangan lupa latihan lagi")


print ("\n --- batas --- \n")



# Studi kasus nilai rapor UTS

nilai = int (input ("Masukkan nilai UTS kamu sekarang = "))

if nilai >= 100 and nilai <= 90:
    print (f"Nilai kamu sangat memuaskan, nilai = {nilai}")

elif nilai >= 89 and nilai <= 80:
    print (f"Nilai kamu lumayan bagus, nilai = {nilai}")

elif nilai >= 79 and nilai <= 60:
    print (f"Nilai kamu cukup jelek, nilai = {nilai}")

elif nilai >= 59 and nilai <= 50:
    print (f"Nilai kamu jelek kali, nilai = {nilai}")

elif nilai >= 49 and nilai <= 40:
    print (f"Nilai kamu jelek banget, nilai = {nilai}")

elif nilai >= 39 and nilai <= 30:
    print (f"Nilai kamu sangat buruk, nilai = {nilai}")

else:
    print (f"Input tidak valid, nilai = {nilai}")
    print ("Selamat and sudah selesai dengan program itu")


print ("\n --- batas --- \n")



# Studi kasus nilai usia produktif manusia saat ini

usia_kamu = int (input ("Masukkan usia kamu saat ini = "))

if usia_kamu >= 15 and usia_kamu <= 40:
    print (f"Kamu sudah termasuk usia produktif manusia, usia = {usia_kamu}")

elif usia_kamu > 40:
    print (f"Kamu masuk usia sudah tua, usia = {usia_kamu}")

elif usia_kamu < 15:
    print (f"Usia kamu masih kecil, usia = {usia_kamu}")

else:
    print (f"Input tidak valid, usia = {usia_kamu}")


print ("\n --- batas --- \n")



# Studi kasus tentang Usia dan jenjang kehidupan manusia

usia_anda = int (input ("Masukkan usia anda = "))

if usia_anda >= 1 and usia_anda <= 4:
    print (f"Masih balita, usia anda = {usia_anda}")

elif usia_anda >= 5 and usia_anda <= 11:
    print (f"Anak-anak, usia anda = {usia_anda}")

elif usia_anda >= 12 and usia_anda <= 14:
    print (f"Pra remaja, usia anda = {usia_anda}")

elif usia_anda >= 15 and usia_anda <= 19:
    print (f"Remaja, usia anda = {usia_anda}") 

elif usia_anda >= 20 and usia_anda <= 40:
    print (f"Dewasa, usia = {usia_anda}")

elif usia_anda >= 41 and usia_anda <= 50:
    print (f"Sudah tua dan bukan usia produktif lagi, usia anda = {usia_anda}")

elif usia_anda >= 51 and usia_anda <= 65:
    print (f"Sudah lanjut usia, dan sudah tua, usia anda = {usia_anda}")

else:
    print (f"Input tidak valid, usia anda = {usia_anda}")


print ("\n --- batas --- \n")



# Studi kasus tentang usia jenjang masuk pendidikan dan perguruan tinggi 

usia_lu = int (input ("Masukkan usia lu sekarang = "))

if usia_lu >= 4 and usia_lu <= 6:
    print (f"Usia kamu masuk TK, usia lu = {usia_lu}")

elif usia_lu >= 7 and usia_lu <= 12:
    print (f"Usia kamu sudah masuk SD, usia lu = {usia_lu}")

elif usia_lu >= 13 and usia_lu <= 16:
    print (f"Sudah masuk SMP, usia lu = {usia_lu}")

elif usia_lu >= 17 and usia_lu <= 19:
    print (f"Sudah masuk SMA, usia = {usia_lu}")

elif usia_lu >= 20 and usia_lu <= 24:
    print (f"Sudah masuk kuliah, usia lu = {usia_lu}")

elif usia_lu >= 25 and usia_lu <= 40:
    print (f"Lu sudah kerja dan menikah serta memiliki anak, usia lu = {usia_lu}")

elif usia_lu >= 41 and usia_lu <= 50:
    print (f"Transisi ke masa tua, usia lu = {usia_lu}")

elif usia_lu >= 51 and usia_lu <= 60:
    print (f"Sudah tua usia lu, usia lu = {usia_lu}")

elif usia_lu >= 65 and usia_lu <= 70:
    print (f"Sudah tua banget usia lu, usia lu = {usia_lu}")

elif usia_lu >= 71 and usia_lu <= 80:
    print (f"Usia lu udah tua banget, usia lu = {usia_lu}")

else:
    print (f"Input tidak valid, usia lu = {usia_lu}")


print ("\n --- batas --- \n")



# Studi kasus tentang Prakiraan cuaca saat ini

cuaca = str (input ("Masukkan cuaca hari ini ya = "))
suhu = int (input ("Masukkan suhu hari ini ya = "))

if cuaca == "cerah":
    if suhu > 30:
        print ("Boleh keluar rumah")

    else:
        print ("Jangan keluar rumah")

elif cuaca == "berawan":
    if suhu < 30:
        print ("Cuaca nya adem dan boleh keluar rumah")

    else:
        print ("Jangan keluar")

elif cuaca == "hujan":
    if suhu < 30:
        print ("Jangan keluar rumah")

    else:
        print ("Bawa payung untuk keluar rumah")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")



# Studi kasus pemilihan genre bioskop dan film bioskop

genre_film = str (input ("Masukkan genre bioskop = "))
usia_kamu = int (input ("Masukkan film bioskop = "))

if genre_film == "horor":
    if usia_kamu >= 17 and usia_kamu <= 25:
        print (f"Usia kamu sudah layak, usia = {usia_kamu} dan genre film = {genre_film}")

    else:
        print (f"Jangan nonton dulu, usia kamu = {usia_kamu} dan genre film = {genre_film}")

elif genre_film == "romantis":
    if usia_kamu >= 18 and usia_kamu <= 26:
        print (f"Usia kamu sudah bisa nonton film genre romantis, usia kamu = {usia_kamu} dan genre film = {genre_film}")

    else:
        print (f"Jangan nonton dulu, usia kamu = {usia_kamu} dan genre film = {genre_film}")

elif genre_film == "komedi":
    if usia_kamu >= 16 and usia_kamu <= 26:
        print (f"Usia kamu sudah cukup untuk nonton film komedi, usia kamu = {usia_kamu} dan genre film = {genre_film}")

    else:
        print (f"Jangan dulu, usia kamu = {usia_kamu} dan genre film = {genre_film}")

else:
    print (f"Input tidak valid, usia kamu = {usia_kamu} dan genre film = {genre_film}")


print ("\n --- batas --- \n")



# Array List Dasar + Method Python

daftar = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48", "Lana JKT48", "Erine JKT48"]

daftar.append ("Olla JKT48")
daftar.append ("Jessi JKT48")
daftar.append ("Eli JKT48")
daftar.append ("Mikaela JKT48")
daftar.append ("Oline JKT48")

for f in daftar:
    print (f)

print ("\n --- batas --- \n")




# Studi kasus tentang sistem pembayaran Makanan dan Minuman milik Lambert

print ("""
=============================================================================

Studi kasus tentang sistem pembayaran Makanan dan Minuman milik Lambert

==============================================================================

""")

nasi_goreng = 4000
mie_ayam = 5000
bakso = 7000
pangsit = 6000
mie_goreng = 5000
pop_mie = 2000
mie_soto = 6000
teh_poci_es = 6000
teh_manis_anget = 7000
kopi = 6000


j_kopi = int (input ("Masukkan jumlah kopi sekarang = "))
j_teh_manis_anget = int (input ("Masukkan jumlah teh manis anget = "))
j_teh_poci_es = int (input ("Masukkan jumlah teh poci anget = "))
j_mie_soto = int (input ("Masukkan jumlah mie = "))
j_pop_mie = int (input ("Masukkan jumlah pop mie = "))
j_mie_goreng = int (input ("Masukkan jumlah mie goreng = "))
j_pangsit = int (input ("Masukkan jumlah pangsit = "))
j_bakso = int (input ("Masukkan jumlah bakso = "))
j_mie_ayam = int (input ("Masukkan jumlah mie ayam = "))
j_nasi_goreng = int (input ("Masukkan jumlah nasi goreng = "))


a1 = kopi * j_kopi
a2 = bakso * j_bakso
a3 = nasi_goreng * j_nasi_goreng
a4 = pangsit * j_pangsit
a5 = teh_manis_anget *j_teh_manis_anget
a6 = teh_poci_es * j_teh_poci_es
a7 = pop_mie * j_pop_mie
a8 = mie_soto * j_mie_soto
a9 = mie_goreng * j_mie_goreng
a10 = mie_ayam * j_mie_ayam

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total

cek = uang_kamu > total


rincian_bayar = f"""
==================================================================================

RINCIAN PEMBAYARAN YANG DETAIL 

=================================================================================


\n Uang kamu sekarang   : {uang_kamu}
\n Total uang sekarang  : {total}
\n Kembalian uang       : {kembalian}
\n Cek                  : {cek}


"""

print (rincian_bayar)


print ("\n --- batas --- \n")