print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Helo Dunia"
print (a)

b = "Halo Fun"
print (b)


c = True
print (c)

print ("\n --- batas --- \n")



# Cek tipe data pemrograman

print ("Teks =", type (a))
print ("Angka =", type (b))
print ("Cek =", type (c))


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
print ("Bagi =", bagi (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))

print ("\n --- batas --- \n")



# Studi kasus fungsi return mencari angka terkecil

def angka_kecil (f, k):

    if f < k:
        return f

    else:
        return k

print ("Angka kecil =", angka_kecil (10, 5))
print ("Angka kecil =", angka_kecil (4, 32))
print ("Angka kecil =", angka_kecil (90, 3))
print ("Angka kecil =", angka_kecil (30, 5))
print ("Angka kecil =", angka_kecil (90, 6))


print ("\n --- batas --- \n")




# Studi kasus fungsi return dengan mencari angka terbesar

def angka_besar (r, t):

    if r > t:
        return r

    else:
        return t

print ("Angka besar =", angka_besar (50, 4))
print ("Angka besar =", angka_besar (40, 9))
print ("Angka besar =", angka_besar (90, 8))
print ("Angka besar =", angka_besar (40, 3))
print ("Angka besar =", angka_besar (45, 3))


print ("\n --- batas --- \n")


# Switch Case dengan lampu lalu lintas

lalin = str (input ("Masukkan warna lampu lintas"))

match (lalin):

    case "Merah":
        print ("Berhenti, warna merah")

    case "Kuning":
        print ("Hati-hati, warna kuning")

    case "Hijau":
        print ("Jalan, warna hijau")

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")



# Studi kasus perasaan manusia 

perasaan = str (input ("Masukkan perasaan kamu sekarang ini = "))

match (perasaan):

    case "Marah":
        print ("Marah")

    case "Sedih":
        print ("Sedih")

    case "Nangis":
        print ("Nangis")

    case "Biasa aja":
        print ("Biasa aja")

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")




# Studi kasus percabangan tentang prakiraan cuaca 

cuaca = str (input ("Masukkan cuaca hari ini = "))
suhu = int (input ("Masukkan suhu dalam celcius = "))

if cuaca == "cerah":
    if suhu > 30:
        print ("Boleh keluar rumah")

    else:
        print ("Gak boleh rumah")

elif cuaca == "berawan":
    if suhu < 30:
        print ("Boleh keluar rumah")

    else:
        print ("dingin udara di luar")

elif cuaca == "hujan":
    if suhu < 30:
        print ("Bawa payung atau jas hujan")

    else:
        print ("Jangan keluar rumah")

else:
    print ("Input tidak valid")


akhir_input = f"""
- cuaca hari {cuaca} dan suhu hari ini {suhu}
"""

print (akhir_input)


print ("\n --- batas --- \n")




# Studi kasus percabangan pemilihan jenjang pendidikan kamu

usia = int (input ("Masukkan usia kamu sekarang ini = "))
jenjang = str (input ("Masukkan jenjang pendidikan kamu = "))


if jenjang == "tk":
    if usia >= 4 and usia <= 6:
        status = "tk"
        print ("masuk tk sekarang")

    else:
        print ("belum masuk tk")

elif cuaca == "sd":
    if usia >= 6 and usia <= 15:
        status = "sd"
        print ("Boleh masuk sd")

    else:
        print ("masih tk")

elif cuaca == "smp":
    if usia >= 15 and usia <= 17:
        status = "smp"
        print ("Masuk smp")

    else:
        print ("Masih sd")

elif cuaca == "sma":
    if usia >= 17 and usia <= 19:
        status = "sma"
        print ("Masuk sma")

    else:
        print ("Masih smp")

elif jenjang == "kuliah":
    if usia >= 19 and usia <= 26:
        status = "kuliah"
        print ("Masuk kuliah")

    else:
        print ("Masih SMA")

elif jenjang == "kerja":
    if usia >= 26 and usia <= 45:
        status = "kerja"
        print ("Masuk kerja")

    else:
        print ("Masih kuliah")

elif jenjang == "lanjut usia":
    if usia >= 45 and usia <= 75:
        status = "lanjut usia"
        print ("Sudah masuk lanjut usia")

    else:
        print ("Masih kerja")

else:
    print ("Input tidak valid")

usia_manusia = f"""
- Kamu sekarang lagi {jenjang} dengan usia {usia} tahun
"""

print (usia_manusia)

print ("\n --- batas --- \n")



# Studi kasus percabangan pemilihan genre film dan harganya

genre_film = str (input ("Masukkan genre film = "))
harga_film = int (input ("Masukkan harga film = "))
usia_kamu = int (input ("Masukka usia kamu saat kamu mau nonton = "))

if genre_film == "keluarga":
    if usia >= 2 and usia <= 20:
        harga = 5000
        print ("Boleh nonton film keluarga")

    else:
        print ("Nonton film yang lain aja")

elif genre_film == "animasi":
    if usia >= 5 and usia <= 30:
        harga = 7000
        print ("Boleh nonton film sekarang")

    else:
        print ("Nonton film yang lain yang lebih pas")

elif genre_film == "komedi":
    if usia >= 15 and usia <= 20:
        harga = 6000
        print ("Boleh nonton komedi")

    else:
        print ("Gak boleh nonton sekarang")

elif genre_film == "hero":
    if usia >= 10 and usia <= 25:
        harga = 6000
        print ("Boleh nonton film hero")

    else:
        print ("Gak boleh nonton")

elif genre_film == "romantis":
    if usia >= 19 and usia <= 25:
        harga = 7000
        print ("Boleh nonton film romantis")

    else:
        print ("Gak boleh nonton film romantis")

elif genre_film == "dokumenter":
    if usia >= 15 and usia <= 20:
        harga = 7000
        print ("Boleh nonton dokumenter")

    else:
        print ("Gak boleh nonton dokumenter")

else:
    print ("Input tidak valid")


rincian_film = f"""
- Kamu nonton bergenre {genre_film} dengan harga film Rp {harga_film}

"""

print (rincian_film)


print ("\n --- batas --- \n")



# Studi kasus percabangan join dan daftar JK48

usia = int (input ("Masukkan usia kamu sekarang ini ="))
jenjang_kamu = str (input ("Masukkan jenjang kamu ini = "))

if jenjang_kamu == "sd":
    if usia >= 13 and usia <= 20:
        print ("Boleh masuk JKT48")

    else:
        print ("jangan dulu ya dek")

elif jenjang_kamu == "smp":
    if usia >= 13 and usia <= 20:
        print ("Boleh masuk jkt48")

    else:
        print ("Jangan dulu ya")

elif jenjang_kamu == "sma":
    if usia >= 13 and usia <= 20:
        print ("Boleh dan join JKT48")

    else:
        print ("Gak boleh join JKT48")

elif jenjang_kamu == "kuliah":
    if usia >= 13 and usia <= 20:
        print ("Boleh join dan daftar JKT48")

    else:
        print ("Jangan dulu gabung")

elif usia > 20:
    print ("Sudah lebih dari cukup untuk join dan daftar JKT48")

else:
    print ("Input tidak valid")


data_akhir = f"""
- Kamu :

jenjang = {jenjang_kamu}
usia = {usia}

"""

print (data_akhir)


print ("\n --- batas --- \n")



# For oshi jkt48

oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48"]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Freya JKT48")
oshi.append ("Olla JKT48")
oshi.append ("Eli JKT48")
oshi.append ("Christy JKT48")
oshi.append ("Marsha JKT48")


for t in oshi:
    print (t)


print ("\n --- batas --- \n")



#  Dictionary

data = {
    "nama" : "Habib Muzakki",
    "asal_daerah" : "Kota Serang",
    "usia" : 19,
    "hobi" : "Ngewota JKT48", 
    "status" : "Oke",
}

print ("Nama :", data ["nama"])
print ("Asal daerah :", data ["asal_daerah"])
print ("Usia kamu :", data ["usia"])
print ("Hobi kamu :", data ["hobi"])
print ("Status kamu :", data ["status"])


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def nama (halo):
    print (f"Halo nama saya {halo} dari Jakarta Pusat")

nama ("Han")
nama ("Roy")
nama ("Far")
nama ("Yan")
nama ("Yun")
nama ("Fer")


print ("\n --- batas --- \n")