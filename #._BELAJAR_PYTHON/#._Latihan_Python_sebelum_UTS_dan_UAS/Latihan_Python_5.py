print ("Hello World")

print ("\n --- batas --- \n")



# Biodata lengkap Habib Muzakki

nama = "Habib Muzakki"
akrab = "Habib"
asal_daerah = "Kota Serang, Banten"
coding = "HTML, CSS, JavaScript, Python"




# variabel dasar

a = "Halo Dunia"
b = 12
c = 12.12
d = True

rio = f"""
- Teks      : {a}
- Angka     : {b}
- Desimal   : {c}
- Cek       : {d}


"""

print (rio)

print ("\n --- batas --- \n")




# Tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
- Teks      : {teks}
- Angka     : {angka}
- Desimal   : {desimal}
- Cek       : {cek}
"""

print (tipe)

print ("\n --- batas --- \n")




# Cek tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")





# Operator dasar 

a = int (input ("Masukkan angka a = "))
b = int (input ("Masukkan angka b = "))

print ("Tambah =", a + b)
print ("Kurang =", a - b)
print ("Kali =", a * b)
print ("Bagi =", a / b)
print ("Pangkat =", a ** b)
print ("Modulus =", a % b)


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



# Switch Case dengan rambu lalu lintas sederhana

lampu = str (input ("Masukkan warna lampu lalu lintas = "))

match (lampu):

    case "merah":
        print ("Berhenti, lampu merah menyala")

    case "kuning":
        print ("Hati-hati, lampu kuning menyala")

    case "hijau":
        print ("Jalan, lampu hijau menyala")

    case _:
        print ("Lampu lalu lintas tidak menyala, berhati-hati")

print ("\n --- batas --- \n")



# Switch Case dengan nama-nama hari dalam seminggu

hari = str (input ("Masukkan nama hari dalam seminggu = "))

match (hari):

    case "senin":
        print ("Hari ini adalah hari senin")

    case "selasa":
        print ("Hari ini adalah hari selasa")

    case "rabu":
        print ("Hari ini adalah hari rabu")

    case "kamis":
        print ("Hari ini adalah hari kamis")

    case "jumat":
        print ("Hari ini adalah hari jumat")

    case "sabtu":
        print ("Hari ini adalah hari sabtu")

    case "minggu":
        print ("Hari ini adalah hari minggu")

    case _:
        print ("Hari yang kamu masukkan tidak ada dalam seminggu")

print ("\n --- batas --- \n")



# Switch Case dengan nama-nama bulan dalam setahun

bulan = str (input ("Masukkan nama bulan dalam setahun = "))

match (bulan):

    case "januari":
        print ("Bulan ini adalah bulan januari")

    case "februari":
        print ("Bulan ini adalah bulan februari")

    case "maret":
        print ("Bulan ini adalah bulan maret")

    case "april":
        print ("Bulan ini adalah bulan april")

    case "mei":
        print ("Bulan ini adalah bulan mei")

    case "juni":
        print ("Bulan ini adalah bulan juni")

    case "juli":
        print ("Bulan ini adalah bulan juli")

    case "agustus":
        print ("Bulan ini adalah bulan agustus")

    case "september":
        print ("Bulan ini adalah bulan september")

    case "oktober":
        print ("Bulan ini adalah bulan oktober")

    case "november":
        print ("Bulan ini adalah bulan november")

    case "desember":
        print ("Bulan ini adalah bulan desember")

    case _:
        print ("Bulan yang kamu masukkan tidak ada dalam setahun")

print ("\n --- batas --- \n")



# Percabangan dasar

a = 9

if a >= 5:
    print (f"Besar, angka a = {a}")

else:
    print (f"Kecil, angka a = {a}")


print ("\n --- batas --- \n")



# Percabangan lanjutan

b = 3

if b >= 8:
    print (f"Besar, angka b = {b}")

elif b >= 5:
    print (f"Sedang, angka b = {b}")

else:
    print (f"Kecil, angka b = {b}")


print ("\n --- batas --- \n")



# Studi Kasus Usia Join JKT48

usia = int (input ("Masukkan usia kamu sekarang = "))

if usia >= 13 and usia <= 20:
    print (f"Selamat, kamu bisa join JKT48, usia kamu = {usia}")

elif usia > 20:
    print (f"Maaf, kamu sudah terlalu tua untuk join JKT48, usia kamu = {usia}")

else:
    print (f"Maaf, kamu masih terlalu muda untuk join JKT48, usia kamu = {usia}")


print ("\n --- batas --- \n")



# Studi kasus usia masuk kerja

usia = int (input ("Masukkan ujian kamu sekarang = "))

if usia >= 19 and usia <= 45:
    print (f"Selamat, kamu ujian kerja, usia kamu = {usia}")

elif usia > 45:
    print (f"Maaf, kamu sudah terlalu tua untuk ujian kerja, usia kamu = {usia}")

else:
    print (f"Maaf, kamu masih terlalu muda untuk ujian kerja, usia kamu = {usia}")


print ("\n --- batas --- \n")




# Studi kasus usia masuk kuliah

usia_kuliah = int (input ("Masukkan usia kamu sekarang = "))

if usia_kuliah >= 16 and usia_kuliah <= 25:
    print (f"Selamat, kamu bisa masuk kuliah, usia kamu = {usia_kuliah}")

elif usia_kuliah > 25:
    print (f"Maaf, kamu sudah terlalu tua untuk masuk kuliah, usia kamu = {usia_kuliah}")

else:
    print (f"Maaf, kamu masih terlalu muda untuk masuk kuliah, usia kamu = {usia_kuliah}")


print ("\n --- batas --- \n")



# Studi kasus nilai ujian UTS D4 Teknik Informatika

nilai = int (input ("Masukkan nilai ujian kamu = "))

if nilai >= 90:
    print (f"A, nilai ujian kamu = {nilai}")

elif nilai >= 80:
    print (f"B, nilai ujian kamu = {nilai}")

elif nilai >= 70:
    print (f"C, nilai ujian kamu = {nilai}")

elif nilai >= 60:
    print (f"D, nilai ujian kamu = {nilai}")

elif nilai >= 50:
    print (f"E, nilai ujian kamu = {nilai}")

elif nilai >= 40:
    print (f"F, nilai ujian kamu = {nilai}")

else:
    print (f"Maaf, kamu tidak lulus ujian, nilai ujian kamu = {nilai}")


print ("\n --- batas --- \n")




print ("""
===================================================================================

STUDI KASUS CUACA HARI INI

===================================================================================

""")

cuaca = str (input ("Masukkan cuaca hari ini =  (hujan, berawan, cerah) = "))
suhu = int (input ("Masukkan suhu hari ini = "))

if cuaca == "hujan":
    if suhu > 30:
        print (f"Cuaca hari ini adalah hujan dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa payung")

    else:
        print (f"Cuaca hari ini adalah hujan dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa jas hujan")

elif cuaca == "berawan":
    if suhu > 30:
        print (f"Cuaca hari ini adalah berawan dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa payung")

    else:
        print (f"Cuaca hari ini adalah berawan dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa jas hujan")

elif cuaca == "cerah":
    if suhu > 30:
        print (f"Cuaca hari ini adalah cerah dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa topi")

    else:
        print (f"Cuaca hari ini adalah cerah dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa jaket")

else:
    print (f"Cuaca hari ini tidak diketahui dan suhu hari ini adalah {suhu} derajat celcius, jangan lupa bawa payung")


print ("\n --- batas --- \n")




print ("""
=====================================================================================

STUDI KASUS WARUNG KOPI DAN MAKAN MILIK NIKSON NTT

====================================================================================
""")

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))


kopi = 4000
kentang = 5000
nasi_goreng = 6000
nasi_ayam_bakar = 7000
nasi_ayam_goreng = 9000
nasi_ayam_geprek = 10000

j_kopi = int (input ("Masukkan jumlah kopi yang dibeli = "))
j_kentang = int (input ("Masukkan jumlah kentang yang dibeli = "))
j_nasi_goreng = int (input ("Masukkan jumlah nasi goreng yang dibeli = "))
j_nasi_ayam_bakar = int (input ("Masukkan jumlah nasi ayam bakar yang dibeli = "))
j_nasi_ayam_goreng = int (input ("Masukkan jumlah nasi ayam goreng yang dibeli = "))
j_nasi_ayam_geprek = int (input ("Masukkan jumlah nasi ayam geprek yang dibeli = "))


a1 = j_kentang * kentang
a2 = j_nasi_goreng * nasi_goreng
a3 = j_nasi_ayam_bakar * nasi_ayam_bakar
a4 = j_nasi_ayam_goreng * nasi_ayam_goreng
a5 = j_nasi_ayam_geprek * nasi_ayam_geprek
a6 = j_kopi * kopi


total = a1 + a2 + a3 + a4 + a5 + a6

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_belanja = f"""
===================================================================================

RINCIAN BELANJA TOTAL KESELURUHAN NYA

===================================================================================

\n - Nama pemesan 1         : {nama_pemesan1}
\n - Nama pemesan 2         : {nama_pemesan2}   
\n - Nama pemesan 3         : {nama_pemesan3}
\n - Total uang kamu        : {total}
\n - Uang kamu              : {uang_kamu}
\n - Kembalian              : {kembalian}
\n - Cek uang kamu cukup ?  : {cek}

"""

print (rincian_belanja)


print ("\n --- batas --- \n")


print ("""
=============================================================================

TERIMAKASIH ATAS INFORMASI NYA DIATAS

DAN SELALU SEMANGAT TIAP HARI NYA

DAN JANGAN LUPA KERJAKAN TUGAS YANG DITUGASKAN

""")