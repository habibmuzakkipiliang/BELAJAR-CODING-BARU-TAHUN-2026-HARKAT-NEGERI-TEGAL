print ("Hello World")

print ("\n --- batas --- \n")



# Biodata Lengkap Habib Muzakki

nama = "Habib Muzakki"
akrab = "Habib"
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
coding = "HTML, CSS, JavaScript dan Python dan TypeScript"
hobi = "JKT48 dan suka dengan Oshi JKT48 yang cantik-cantik amat"
usia = "19 tahun"
asal_daerah = "Kota Serang, Banten"
marga = "Piliang"
suku = "Minangkabau"


biodata = f"""
\n Nama lengkap     : {nama}
\n Nama panggilan   : {akrab}
\n Asal daerah      : {asal_daerah}
\n Kelas            : {kelas}
\n Jurusan          : {jurusan}
\n Fakultas         : {fakultas}
\n Coding           : {coding}
\n Hobi             : {hobi}
\n Usia kamu        : {usia}
\n Marga            : {marga}
\n Suku daerah      : {suku}
"""
print (biodata)

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia yang indah"
print (a)

b = "Halo yang oke"
print (b)

c = "Halo Fun"
print (c)

d = 12
print (d)


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



# Cek Tipe data pemrograman

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


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")





# Percabangan dasar

a = int (input ("Masukkan angka a = "))

if a >= 8:
    print (f"Angka besar, angka a = {a}")

else:
    print (f"Angka kecil, angka a = {a}")


print ("\n --- batas --- \n")




# angka minus, angka positif dalam percabangan lanjutan

angka = int (input ("Masukkan angka bulat = "))

if angka > 0:
    print (f"Angka positif, angka = {angka}")

elif angka < 0:
    print (f"Angka negatif, angka = {angka}")

else:
    print (f"Angka nol, angka = {angka}")


print ("\n --- batas --- \n")




# Percabangan nested usia produktif manusia

usia = int (input ("Masukkan usia kamu saat ini = "))
cek = True

if usia >= 15 and usia <= 45:
    if cek:
        print (f"usia kamu sudah produktif, usia = {usia}")

    elif usia > 45:
        print (f"usia sudah tua, usia = {usia}")

else:
    print (f"Usia masih anak-anak, usia = {usia}")


print ("\n --- batas --- \n")



# Percabangan nested, usia masuk JKT48 dan daftar resmi

usia_now = int (input ("Masukkan usia kamu sekarang = "))
cek = True

if usia_now >= 13 and usia_now <= 25:
    if cek:
        print (f"Usia kamu sudah cukup untuk join JKT48, usia = {usia_now}")

    elif usia_now > 25:
        print (f"Usia kamu sudah lebih dari cukup, usia = {usia_now}")

else:
    print (f"Masih kecil usia kamu sekarang, usia = {usia_now}")


print ("\n --- batas --- \n")



# Percabangan Prakiraan cuaca hari ini

cuaca = str (input ("Masukkan cuaca nya = "))
suhu = int (input ("Masukkan suhu nya dalam celcius = "))

if cuaca == "cerah":
    if suhu > 30:
        print (f"boleh keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Harus pakai topi, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"Cuaca nya adem nih, boleh jalan-jalan, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Di rumah aja, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Harus bawa payung, cuaca = {cuaca} dan suhu  = {suhu}")

    else:
        print (f"Di rumah aja, cuaca = {cuaca} dan usia = {usia}")

else:
    print (f"Input tidak valid, cuaca = {cuaca} dan usia = {usia}")



print ("\n --- batas --- \n")




# Switch Case dengan lampu merah 

lampu = str (input ("Masukkan warna lampu lalu lintas nya = ")
)

match (lampu):

    case "Merah":
        print ("Merah, berhenti")

    case "Kuning":
        print ("Kuning, hati-hati")

    case "Hijau":
        print ("Hijau, jalan")

    case _:
        print ("Warna lain")


print ("\n --- batas --- \n")





# Switch Case dengan nomor random

angka_random = int (input ("Masukkan angka random aja = "))

match (angka_random):

    case 1:
        print (1)

    case 2:
        print (2)

    case 3:
        print (3)

    case 4:
        print (4)

    case 5:
        print (5)

    case _:
        print ("Angka lain")


print ("\n --- batas --- \n")




# Studi kasus tentang pemilihan buku dan pembayaran buku

jenis_buku = [
    "Majalah",
    "Novel",
    "Buku paket",
    "Buku Komik",
    "Buku Pelajaran",
]

for i in jenis_buku:
    print (i)


buku = str (input ("Masukkan buku sekarang = "))

if buku == "Novel":
    harga = 10000
    print ("Kamu pilih novel")

elif buku == "Majalah":
    harga = 3000
    print ("Pilih majalah")

elif buku == "Buku paket":
    harga = 3000
    print ("Pilih buku paket")

elif buku == "Buku komik":
    harga = 4000
    print ("Pilih buku komik")

elif buku == "Buku Pelajaran":
    harga = 90000
    print ("Pilih buku paket")

else:
    print ("Tidak bisa di input")

pilihan_buku = {buku}

pilihan_buku_biaya = {buku} * {harga}

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian_uang = uang_kamu - pilihan_buku_biaya

cek = uang_kamu > pilihan_buku_biaya

rincian_biaya = f"""
- Total semua   : {pilihan_buku_biaya}
- Kembalian     : {kembalian_uang}
- Cek           : {cek}

"""

print (rincian_biaya)


print ("\n --- batas --- \n")

