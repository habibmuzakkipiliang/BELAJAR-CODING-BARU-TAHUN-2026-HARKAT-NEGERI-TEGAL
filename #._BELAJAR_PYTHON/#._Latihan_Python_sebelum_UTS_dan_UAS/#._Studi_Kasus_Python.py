print ("Hello World")

print ("\n --- batas --- \n")


# studi kasus percabangan nonton bioskop dengan harga, genre, usia dan tempat bioskop nya

harga = int (input ("Masukkan harga sekarang = "))
genre = str (input ("Masukkan genre sekarang = "))
usia = int (input ("Masukkan usia kamu srkarang "))
tempat_bioskop = str (input ("Masukkan tampat bioskop sekarang = "))

if genre == "komedi":
    if usia >= 13 and usia <= 19:
        if tempat_bioskop == "mall":
            harga = 5000
            print ("Boleh nonton film sekarang")

        else:
            print ("Jangan nonton dulu")

elif genre == "romantis":
    if usia >= 18 and usia <= 25:
        if tempat_bioskop == "mal biasa":
            harga = 8000
            print ("Boleh nonton")

        else:
            print ("Jangan nonton dulu")

elif genre == "kartun":
    if usia >= 5 and usia <= 20:
        if tempat_bioskop == "cinepolis":
            harga = 9000
            print ("Boleh nonton kartun")

        else:
            print ("Jangan nonton dulu")

elif genre == "scifi robotik":
    if usia >= 19 and usia <= 30:
        if tempat_bioskop == "mall biasa":
            harga = 9000
            print ("Boleh nonton scifi robotik")

        else:
            print ("Jangan dulu ya bang")

elif genre == "robot perang":
    if usia >= 19 and usia <= 30:
        if tempat_bioskop == "mall besar":
            harga = 220000
            print ("Boleh nonton film itu")

        else:
            print ("Jangan nonton film itu dek")

elif genre == "perang dunia 1":
    if usia >= 20 and usia <= 40:
        if tempat_bioskop == "bioskop keren":
            harga = 30000
            print ("Boleh nonton sekarang")

        else:
            print ("Jangan nonton dulu ya dek")

elif genre == "perang dunia 2":
    if usia >= 20 and usia <= 45:
        if tempat_bioskop == "amerika serikat":
            harga = 7000
            print ("Boleh nonton film itu")

        else:
            print ("Jangan nonton ya dek")

elif genre == "thriller":
    if usia >= 20 and usia <= 45:
        if tempat_bioskop == "mall of serang":
            harga = 5000
            print ("Boleh nonton dong")

        else:
            print ("Jangan nonton dulu ya dek")

elif genre == "jkt48":
    if usia >= 13 and usia <= 20:
        if tempat_bioskop == "fx sudirman":
            harga = 90000
            print ("Boleh nonton sekarang di Fx Sudirman")

        else:
            print ("Harus ditemani orang dewasa untuk nonton itu")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")