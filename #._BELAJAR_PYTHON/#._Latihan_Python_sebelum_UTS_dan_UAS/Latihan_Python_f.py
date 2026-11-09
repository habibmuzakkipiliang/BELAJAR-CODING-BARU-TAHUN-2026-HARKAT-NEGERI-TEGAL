print ("Hello World")


print ("\n --- batas ---- \n")



# variabel dasar

a = "Halo Dunia"
print (a)

b = 12
print (b)

c = 12.12
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# fungsi dengan operator dasar

x = int (input ("Masukkan angka x =  "))
y = int (input ("Masukkan angka y =  "))

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




# Studi kasus tentang Warung Kopi bahagia milik Nikson NTT

print ("""
====================================================================================

STUDI KASUS TENTANG WARUNG KOPI BAHAGIA MILIK NIKSON NTT


=====================================================================================

""")

kopi = 4000
kentang = 5000
aqua = 3000
salad = 4000
nasi_goreng = 4000
mie_goreng = 5000
mie_ayam = 3000
bakso = 3000
mie_kuah = 5000
pop_mie = 1000


nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 ="))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))


j_kopi = int (input ("Masukkan jumlah kopi = "))
j_kentang = int (input ("Masukkan jumlah kentang = "))
j_aqua = int (input ("Masukkan jumlah aqua = "))
j_salad = int (input ("Masukkan jumlah salad ="))
j_nasi_goreng  = int (input ("Masukkan nasi goreng = "))
j_mie_goreng = int (input ("Masukkan mie goreng = "))
j_mie_ayam = int (input ("Masukkan mie ayam = "))
j_bakso = int (input ("Masukkan bakso = "))
j_mie_kuah = int (input ("Masukkan mie ayam = "))
j_pop_mie = int (input ("Masukkan pop mie ="))


a1 = j_aqua * aqua
a2 = j_bakso * bakso
a3 = j_kentang * kentang
a4 = j_kopi * kopi
a5 = j_mie_ayam * mie_ayam
a6 = j_mie_kuah * j_mie_kuah
a7 = j_nasi_goreng * nasi_goreng
a8 = j_pop_mie * pop_mie 
a9 = j_salad * salad


total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_bayar = f"""
\n Nama pemesan 1               : {nama_pemesan1}
\n Nama pemesan 2               : {nama_pemesan2}
\n Nama pemesan 3               : {nama_pemesan3}
\n - Total uang kamu semua      : {total}
\n - Kembalian                  : {kembalian}
\n - Cek                        : {cek}

"""

print (rincian_bayar)

print ("\n --- bayar --- \n")




print ("""
===================================================================================

PERCABANGAN UNTUK CUACA HARI INI SEKARANG

===================================================================================

""")

cuaca = str (input ("Masukkan cuaca hari ini = (cerah, berawan, hujan)"))
suhu = int (input ("Masukkan suhu hari ini dalam celcius = "))

if cuaca == "cerah":
    if suhu > 30:
        print (f"Cuaca nya panas dan cerah, cuaca = {cuaca} dan suhu = {suhu}")
    else:
        print (f"Harus pakai topi mas, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"Sudah adem boleh olahrage joging tipis-tipis, cuaca = {cuaca} dan suhu = {suhu}")
    else:
        print (f"Gak boleh keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Jangan keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")
    else:
        print (f"Harus bawa payung, cuaca = {cuaca} dan suhu = {suhu}")

else:
    print (f"Input tidak valid, cuaca = {cuaca} dan suhu = {suhu}")


print ("\n --- batas --- \n")



print ("""
===============================================================================

PERCABANGAN NONTON BIOSKOP DENGAN NESTED 

================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang = "))
genre = str (input ("Masukkan genre kamu sekarang = "))
cek = True

if genre == "horor":
    if usia >= 13 and usia <= 19:
        if cek:
            print (f"Maka boleh nonton filem horor sekarang, genre = {genre} dan usia = {usia}")

        else:
            print (f"Maka jangan nonton dulu, usia = {usia} dan genre = {genre}")

elif genre == "thriller":
    if usia >= 19 and usia <= 30:
        print (f"Boleh nonton thriller, usia = {usia} dan genre = {genre}")

    else:
        print (f"Jangan nonton dulu, genre = {genre} dan usia = {usia}")

elif genre == "romantis":
    if usia >= 18 and usia <= 35:
        print (f"Boleh nonton romantis, usia = {usia} dan genre = {genre}")

    else:
        print (f"Jangan nonton dulu, usia = {usia} dan genre = {genre}")

elif genre == "komedi":
    if usia >= 17 and usia <= 30:
        print (f"Boleh nonton komedi, usia = {usia} dan genre = {genre}")

    else:
        print (f"Jangan nonton dulu, usia = {usia} dan genre = {genre}")

elif genre == "kartun":
    if usia >= 5 and usia <= 20:
        print (f"Boleh nonton dong, usia = {usia} dan genre = {genre}")

    else:
        print (f"Jangan nonton dulu, usia = {usia} dan genre = {genre}")

else:
    print (f"Input tidak valid, usia = {usia} dan genre = {genre}")


print ("\n --- batas --- \n")




print ("""
==================================================================================

STUDI KASUS TENTANG PERCABANGAN USIA PRODUKTIF DENGAN NESTED

=================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang ini = "))
cek = True

if usia >= 15 and usia <= 40:
    if cek:
        print (f"Sudah masuk usia produktif manusia, usia = {usia}")

    else:
        print (f"Masih remaja, usia = {usia}")

else:
    print (f"Masih kecil usia kamu, usia = {usia}")


print ("\n --- batas --- \n")




print ("""
==================================================================================

SISTEM PENILAIAN RAPOR BIASA 

=================================================================================

""")

rapor = int (input ("Masukkan nilai rapor kamu = "))

if rapor >= 90:
    print (f"A, nilai = {rapor}")

elif rapor >= 80:
    print (f"B, nilai = {rapor}")

elif rapor >= 70:
    print (f"C, nilai = {rapor}")

elif rapor >= 60:
    print (f"D, nilai = {rapor}")

elif rapor >= 50:
    print (f"E, nilai = {rapor}")

elif rapor >= 40:
    print (f"F, nilai = {rapor}")

else:
    print (f"Input tidak valid, nilai = {rapor}")


print ("\n --- batas --- \n")




print ("""
============================================================

PERCABANGAN SKOR SNBT 

============================================================

""")

skor = int (input ("Masukkan skor UTBK kamu sekarang ini = "))

if skor >= 900:
    print (f"A, skor = {skor}")

elif skor >= 800:
    print (f"B, skor = {skor}")

elif skor >= 700:
    print (f"C, skor = {skor}")

elif skor >= 600:
    print (f"D, skor = {skor}")

elif skor >= 500:
    print (f"E, skor = {skor}")

elif skor >= 400:
    print (f"F, skor = {skor}")

else:
    print (f"Input tidak valid, skor = {skor}")


print ("\n --- batas --- \n")