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