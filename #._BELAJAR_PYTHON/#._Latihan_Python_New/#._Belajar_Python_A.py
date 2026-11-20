print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

sore = "Halo Sore hari"
malam = "Halo malam hari"
pagi = "Halo pagi hari"
siang = "Halo siang hari"

print (sore)
print (malam)
print (pagi)
print (siang)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 23.2
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




# Biodata Habib Muzakki

nama_lengkap = "Habib Muzakki"
nama_panggilan = "Habib"
asal_daerah = "Kota Serang, Banten"
coding_saya = "HTML, CSS, JavaScript dan Python"
asal_sekolah = "MAN 2 KOTA SERANG"
jurusan_kuliah = "D4 Vokasi Teknik Informatika"
fakultas_kuliah = "Sekolah Vokasi"
kelas_kuliah = "1B"


profil = f"""
\n Nama lengkap     : {nama_lengkap}
\n Nama panggilan   : {nama_panggilan}
\n Asal Daerah      : {asal_daerah}
\n Coding saya      : {coding_saya}
\n Asal sekolah     : {asal_sekolah}
\n Jurusan kuliah   : {jurusan_kuliah}
\n Fakultas Kuliah  : {fakultas_kuliah}
\n Kelas kuliah     : {kelas_kuliah}

"""

print (profil)

print ("\n --- batas --- \n")



# Switch Case dengan lampu lalu lintas

lampu_lintas = str (input ("Masukkan warna lampu lalu lintas nya = "))

match (lampu_lintas):

    case "Merah":
        print ("Warna merah")

    case "Kuning":
        print ("Warna kuning")

    case "Hijau":
        print ("Warna hijau")

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")



# Switch Case dengan angka 

angka = int (input ("Masukkan angka random 1 = "))

match (angka):

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

    case 6:
        print (6)

    case 7:
        print (7)

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")


# Percabangan Nested 

angka = int (input ("Masukkan angka random = "))
cek = True

if angka >= 5:
    if cek == True:
        print (f"Angka oke, angka = {angka}")

    else:
        print (f"Angka kurang oke, angka = {angka}")

else:
    print (f"Angka belum, angka = {angka}")


print ("\n --- batas --- \n")



# Percabangan dasar

angka = int (input ("Masukkan angka pertama kamu = "))

if angka >= 5:
    print (f"Angka besar, angka = {angka}")

else:
    print (f"Angka kecil, angka = {angka}")


print ("\n --- batas --- \n")



# Percabangan Lanjutan

angka_1 = int (input ("Masukkan angka 1 = "))

if angka_1 > 0:
    print (f"Angka positif, angka = {angka_1}")

elif angka_1 < 0:
    print (f"Angka negatif, angka = {angka_1}")

else:
    print (f"Angka nol, angka = {angka_1}")


print ("\n --- batas --- \n")





# Percabangan Lanjutan 

angka_2 = int (input ("Masukkan angka kamu = "))

if angka_2 >= 8:
    print (f"Angka besar, angka 2 = {angka_2}")

elif angka_2 >= 5:
    print (f"Angka setengah, angka = {angka_2}")

else:
    print (f"Angka nol, angka = {angka_2}")


print ("\n --- batas --- \n")



# Percabangan Prakiraan cuaca

suhu = int (input ("Masukkan suhu dalam celcius = "))
cuaca = str (input ("Masukkan cuaca (berawan, suhu, cerah) = "))

if cuaca == "cerah":
    if suhu > 30:
        print (f"Cuaca nya cerah dan boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"Jangan keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "hujan":
    if suhu < 30:
        print (f"Bawa payung jika kamu keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Jangan keluar rumah sekarang, cuaca = {cuaca} dan suhu = {suhu}")

elif cuaca == "berawan":
    if suhu < 30:
        print (f"Boleh keluar rumah nih, sambil jalan-jalan, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Jangan keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

else:
    print (f"Input tidak valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")



# Percabangan usia nonton dan genre film nya 

genre = str (input ("Masukkan genre film nya = "))
usia = int (input ("Masukkan usia kamu = "))

if genre == "keluarga":
    if usia >= 5 and usia <= 15:
        print (f"Boleh nonton film sekarang, usia = {usia} dan genre film = {genre}")

    else:
        print (f"Jangan nonton film itu, dan cari film lain, usia = {usia} dan genre film = {genre}")

elif genre == "komedi":
    if usia >= 10 and usia <= 19:
        print (f"Boleh nonton film komedi, usia = {usia} dan genre film = {genre}")

    else:
        print (f"Jangan nonton film, usia = {usia} dan genre film = {genre}")

elif genre == "romantis":
    if usia >= 20 and usia <= 30:
        print (f"Boleh nonton film, usia = {usia} dan genre film = {genre}")

    else:
        print (f"Jangan nonton film romantis, usia = {usia} dan genre film = {genre}")

elif genre == "kartun":
    if usia >= 2 and usia <= 20:
        print (f"Boleh nonton kartun, usia = {usia} dan genre film = {genre}")

    else:
        print (f"Jangan nonton film, usia = {usia} dan genre film = {genre}")

elif genre == "action":
    if usia >= 20 and usia <= 35:
        print (f"Boleh nonton film action, usia = {usia} dan genre film = {genre}")

    else:
        print (f"Jangan nonton dulu film action nya, usia = {usia} dan genre film = {genre}")

else:
    print (f"Input tidak valid, usia = {usia} dan genre film = {genre}")


print ("\n --- batas --- \n")



# Percabangan usia dan jenjang pendidikan

pendidikan = str (input ("Masukkan jenjang pendidikan kamu sekarang = "))
usia = int (input ("Masukkan usia kamu sekarang = "))

if pendidikan == "tk":
    if usia >= 4 and usia <= 6:
        print (f"masuk tk, usia = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan tk, usia = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "sd":
    if usia >= 7 and usia <= 12:
        print (f"masuk sd, usia = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan sd, usia = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "smp":
    if usia >= 13 and usia <= 15:
        print (f"masuk smp, usia = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan smp, usia = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "sma":
    if usia >= 16 and usia <= 18:
        print (f"masuk sma, usia = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan sma, usia = {usia} dan pendidikan = {pendidikan}")

elif pendidikan == "kuliah":
    if usia >= 19 and usia <= 22:
        print (f"masuk kuliah, usia = {usia} dan pendidikan = {pendidikan}")

    else:
        print (f"bukan anak kuliahan, usia = {usia} dan pendidikan = {pendidikan}")

else:
    print (f"Input tidak valid, usia = {usia} dan pendidikan = {pendidikan}")


print ("\n --- batas --- \n")



# Percabangan usia manusia dan status nya 

usia = int (input ("Masukkan usia kamu sekarang ini = "))
statuk = str (input ("Masukkan status usia kamu = "))

if statuk == "bayi":
    if usia >= 1 and usia <= 3:
        print (f"masuk usia bayi, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia bayi, usia = {usia} dan statuk = {statuk}")

elif statuk == "balita":
    if usia >= 2 and usia <= 4:
        print (f"masuk usia balita, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia balita, usia = {usia} dan statuk = {statuk}")

elif statuk == "anak-anak":
    if usia >= 5 and usia <= 12:
        print (f"masuk usia anak-anak, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia anak-anak, usia = {usia} dan statuk = {statuk}")

elif statuk == "remaja":
    if usia >= 13 and usia <= 19:
        print (f"masuk usia remaja, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia remaja, usia = {usia} dan statuk = {statuk}")

elif statuk == "dewasa":
    if usia >= 19 and usia <= 26:
        print (f"masuk usia dewasa, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia dewasa, usia = {usia} dan statuk = {statuk}")

elif statuk == "dewasa matang":
    if usia >= 27 and usia <= 40:
        print (f"masuk usia dewasa matang, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia dewasa matang, usia = {usia} dan statuk = {statuk}")

elif statuk == "tua":
    if usia >= 40 and usia <= 60:
        print (f"masuk usia tua, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia tua, usia = {usia} dan statuk = {statuk}")

elif statuk == "tua banget":
    if usia >= 60 and usia <= 70:
        print (f"masuk usia tua banget, usia = {usia} dan statuk = {statuk}")

    else:
        print (f"bukan masuk usia tua, usia = {usia} dan statuk = {statuk}")

else:
    print (f"Input tidak valid, usia = {usia} dan statuk = {statuk}")


print ("\n --- batas --- \n")



# For dasar

for a in range (20):
    print (f"urutan ke - {a}")

print ("\n --- batas --- \n")



# for dasar 2

for b in range (1, 30):
    print (f"urutan ke - {b}")


print ("\n --- batas --- \n")



# For dasar 2

for y in range (70):
    print ("Aku suka sama Gracie JKT48 Cantik dan imut")


print ("\n --- batas --- \n")



# For dasar 3

for a in range (80):
    print ("Aku suka dan fans dengan JKT48")


print ("\n --- batas --- \n")