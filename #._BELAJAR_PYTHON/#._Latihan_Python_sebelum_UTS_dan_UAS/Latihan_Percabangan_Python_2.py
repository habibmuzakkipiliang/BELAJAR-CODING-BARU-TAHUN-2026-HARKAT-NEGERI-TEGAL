print ("""
===================================================================================

BIODATA HABIB MUZAKKI SECARA DETAIL

======================================================================================

""")

nama_lengkap = "Habib Muzakki"
nama_panggilan = "Habib"
asal_daerah = "Kota Serang, Banten"
coding = "HTML, CSS, JavaScript dan Python"
kampus = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
hobi = "Ngewota JKT48 dan suka dengan Oshi JKT48"
oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Fritzy JKT48"]


bio = f"""
\n - Nama lengkap   : {nama_lengkap}
\n - Nama panggilan : {nama_panggilan}
\n - Asal daerah    : {asal_daerah}
\n - Coding         : {coding}
\n - Kampus         : {kampus}
\n - Jurusan        : {jurusan}
\n - Fakultas       : {fakultas}
\n - Hobi           : {hobi}
\n - Oshi JKT48     : 

"""

print (bio)


for i in oshi:
    print (i)


print ("\n --- batas --- \n")




# Studi kasus untuk menentukan percabangan usia masuk JKT48 

print ("""
===================================================================================
Usia masuk JKT48 
==================================================================================
""")

usia = int (input ("Masukkan usia kamu untuk join jkt48 = "))
cek = True

if usia >= 13 and usia <= 19:
    if cek:
        print (f"Usia yang sudah cukup untuk join JKT48, usia = {usia}")

    elif usia > 19:
        print (f"Sudah lebih dari cukup, usia = {usia}")

else:
    print (f"Usia kamu masih kecil, usia = {usia}")


print ("\n --- batas --- \n")



# Studi kasus tentang Percabangan usia produktif manusia

print ("""
====================================================

Percabangan usia produktif manusia

=================================================

""")

usia = int (input ("Masukkan usia kamu = "))
cek = True

if usia >= 15 and usia <= 45:
    if cek:
        print (f"Usia yang sudah produktif, usia = {usia}")

    elif usia > 45:
        print (f"Sudah tua usianya, usia = {usia}")

else:
    print (f"Belum masuk usia produktif, usia = {usia}")


print ("\n --- batas --- \n")



# Studi kasus tentang Percabangan Suhu cuaca hari ini

print ("""
====================================================================================

PERCABANGAN SUHU CUACA HARI INI

=====================================================================================

""")

cuaca = str (input ("Masukkan cuaca hari ini (cerah, berawan, hujan) : "))
suhu = int (input ("Masukkan suhu hari ini dalam Celcius : "))

if cuaca == "cerah":
    if suhu > 30:
        print (f"Suhu yang cerah, boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")
    else:
        print (f"Harus bawa payung dan tetap keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"Boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")
    else:
        print (f"Tetap hati-hati keluar rumah dari hujan deras, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Sudah turun hujan dan dingin, suhu = {suhu} dan cuaca = {cuaca}")
    else:
        print (f"Boleh bawa payung, suhu = {suhu} dan cuaca = {cuaca}")

else:
    print ("Input tidak valid sekarang ini")


print ("\n --- batas --- \n")