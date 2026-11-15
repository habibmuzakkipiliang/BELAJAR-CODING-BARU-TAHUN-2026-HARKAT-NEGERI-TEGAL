print ("""
=====================================================================================

PERCABANGAN BELI TIKET BIOSKOP

=====================================================================================

""")

tiket = int (input ("Masukkan harga tiket nya = "))
usia = int (input ("Masukkan usia nya = "))
genre = str (input ("Masukkan genre film nya = "))

if genre == "horor":
    if usia >= 18:
        tiket = 3000
        print (f"Boleh nonton film dan berani, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

    else:
        print (f"Gak boleh nonton film, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

elif genre == "Romantis":
    if usia >= 20:
        tiket = 5000
        print (f"Boleh nonton film, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

    else:
        print (f"Gak boleh nonton film sekarang, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

elif genre == "Thriller":
    if usia >= 23:
        tiket = 5000
        print (f"Boleh nonton film, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

    else:
        print (f"Gak boleh nonton sekarang, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

elif genre == "Drama":
    if usia >= 18:
        tiket = 5000
        print (f"Boleh nonton sekarang, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

    else:
        print (f"Gak boleh nonton film sekarang, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

elif genre == "Komedi":
    if usia >= 19:
        tiket = 4000
        print (f"Boleh nonton film, usia = {usia} dan tiket = {tiket} dan genre = {genre}")

    else:
        print (f"Gak boleh nonton sekarang, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

elif genre == "Animasi":
    if usia >= 5:
        tiket = 1000
        print (f"Boleh nonton untuk anak-anak, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

    else:
        print (f"Nonton dan main game FF, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

elif genre == "Fantasi":
    if usia >= 17:
        tiket = 5000
        print (f"Boleh nonton sekarang, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

    else:
        print (f"Gak boleh nonton sekarang, usia = {usia} dan genre = {genre} dan tiket = {tiket}")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")



print ("""
=====================================================================================

PERCABANGAN PILIH CUACA HARI INI

=====================================================================================

""")

cuaca = str (input ("Masukkan cuaca hari ini (cerah, berawan dan hujan) : "))
suhu = int (input ("Masukkan suhu hari ini dalam celcius :  "))

if cuaca == "hujan":
    if suhu < 30:
        print (f"Jangan keluar rumah, cuaca = {cuaca} dan suhu = {suhu}")

    else:
        print (f"Bawa payung aja, suhu = {suhu} dan cuaca = {cuaca}")

elif cuaca == "cerah":
    if suhu > 30:
        print (f"Boleh keluar rumah, suhu = {suhu} dan cuaca = {cuaca}")

    else:
        print (f"Gak boleh keluar rumah, usia = {usia} dan cuaca = {cuaca}")


elif cuaca == "berawan":
    if suhu < 30:
        print (f"Boleh keluar rumah sambil olahraga santai, usia = {usia} dan cuaca = {cuaca}")

    else:
        print (f"Gak boleh keluar rumah, usia = {usia} dan cuaca = {cuaca}")

else:
    print (f"Gak bisa valid, suhu = {suhu} dan cuaca = {cuaca}")


print ("\n --- batas --- \n")




print ("""
====================================================================================

PERCABANGAN USIA MASUK KERJA 

====================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang = "))

if usia >= 20 and usia <= 45:
    print (f"Usia kamu sudah boleh untuk kerja, usia = {usia}")

elif usia > 45:
    print (f"Sudah tua dan diharuskan untuk pensiun sekarang, usia = {usia}")

else:
    print (f"Masih kecil usia nya, usia = {usia}")


print ("\n --- batas --- \n")




print ("""
======================================================================================

SISTEM MASUK JKT48 dan Persyaratan nya

======================================================================================

""")

usia_kamu = int (input ("Masukkkan usia kamu = "))
cek = True

if usia_kamu >= 13 and usia_kamu <= 19:
    if cek:
        print (f"Boleh masuk jkt48, usia sekarang = {usia_kamu}")

    elif usia_kamu > 19:
        print (f"Sudah lebih dari cukup sekarang, usia = {usia_kamu}")

else:
    print (f"Masih kecil ini, usia = {usia_kamu}")


print ("\n --- batas --- \n")




print ("""
==================================================================================

SISTEM WARNA DALAM LALU LINTAS 

==================================================================================

""")

lampu = int (input ("Masukkan warna nya = "))

match (lampu):

    case "merah":
        print ("Warna Merah")

    case "kuning":
        print ("Warna kuning")

    case "hijau":
        print ("Warna hijau")

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")





print ("""
====================================================================================

SISTEM PEMILIHAN 1 - 10 RANDOM

================================================================================

""")


random_angka = int (input ("Masukkan random angka nya = "))

match (random_angka):

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
        print ("Semula")


print ("\n --- batas --- \n")




print ("""
=========================================================================

PERCABANGAN HARGA DAN USIA BIOSKOP

========================================================================

""")

harga = int (input ("Masukkan harga tiket nya = "))
usia = int (input ("Masukkan usia hari ini = "))
cek = True

if harga >= 30000 and usia >= 18:
    if cek:
        print (f"Boleh nonton dan berkunjung, usia = {usia} dan harga = {harga}")

    elif harga >= 3000 and usia < 18:
        print (f"Boleh nonton dari segi harga, tapi belum cukup dari usia nya, usia =  {usia} dan harga = {harga}")

    elif harga >= 3000 or usia < 18:
        print (f"Boleh ikut karena harga tapi belum karena usia nya, usia = {usia} dan harga = {harga}")

else:
    print (f"Jangan ikut dulu, usia = {usia} dan harga = {harga}")



print ("\n --- batas --- \n")




print ("""
=====================================================================================

USIA MASUK JKT48 DAN JOIN JKT48

=====================================================================================

""")

usia = int (input ("Masukkan usia hari ini = "))
cek = True

if usia >= 13 and usia <= 19:
    if cek:
        print (f"Boleh daftar jkt48, usia = {usia}")

    elif usia > 19:
        print (f"Sudah lebih dari cukup, usia = {usia}")

else:
    print (f"Jangan daftar dulu, usia = {usia}")


print ("\n --- batas --- \n")




print ("""
====================================================================================

PERCABANGAN SISTEM PEMILIHAN MAKANAN

====================================================================================

""")

makanan = str (input ("Masukkan kondisi makanan sekarang = (sehat, rentan, tidak sehat : ) "))
usia = int (input ("Masukkan usia sekarang = "))
cek = True

if makanan == "sehat":
    if usia >= 10 and usia <= 30:
        if cek:
            print (f"Usia dan makanan sudah oke, makanan = {makanan} dan usia = {usia}")

        else:
            print (f"Gak boleh makan dong, makanan = {makanan} dan usia = {usia}")

elif makanan == "rentan":
    if usia >= 10 and usia <= 30:
        print (f"Sudah jangan dulu, makanan = {makanan} dan usia = {usia}")

    else:
        print (f"Ujungnya sakit loh, makanan = {makanan} dan usia = {usia}")


elif makanan == "tidak sehat":
    if usia >= 10 and usia <= 30:
        print (f"Jangan sama sekali, makanan = {makanan} dan usia = {usia}")

    else:
        print (f"Sakit parah bang, makanan = {makanan} dan usia = {usia}")

else:
    print (f"Input tidak valid, usia = {usia} dan makanan = {makanan}")


print ("\n --- batas --- \n")