# Latihan Percabangan Python

print ("""
======================================================================================

Sistem bilangan angka ganjil dan genap 

=====================================================================================
""")

angka = int (input ("Masukkan angka apa aja = "))

if angka % 1 > 2:
    print (f"Angka itu genap, angka = {angka}")

else:
    print (f"Angka itu ganjil, angka = {angka}")

print ("\n --- batas --- \n")




print ("""
=====================================================================================

Sistem Bilangan Diskon Toko

=====================================================================================
""")

total_belanja = int (input ("Masukkan uang kamu = "))

if total_belanja >= 500000 % 100:
    print (f"Maka dapet 20%, total belanja = {total_belanja}")

elif total_belanja >= 200000 % 100:
    print (f"Maka dapet 10%, total belanja = {total_belanja}")

else:
    print (f"Tanpa diskon sama sekali, total belanja = {total_belanja}")


print ("\n --- batas --- \n")



print ("""
==================================================================================

SISTEM MENENTUKA USIA DAN STATUS NYA

======================================================================================

""")

usia = int (input ("Masukkan usia kamu sekarang = "))

if usia >= 13 and usia <= 17:
    print (f"Itu termasuk usia remaja, usia = {usia}")

elif usia > 18:
    print (f"Itu termasuk usia dewasa, usia = {usia}")

else:
    print (f"Itu termasuk masih anak-anak, usia = {usia}")



print ("\n --- batas --- \n")




print ("""
======================================================================================

SISTEM PRAKIRAAN CUACA SEDERHANA

======================================================================================
""")

cuaca = str (input ("Masukkan cuaca hari ini : (cerah, berawan, hujan) : "))
suhu = int (input ("Masukkan suhu udara hari ini : dalam Celcius "))

if cuaca == "cerah":
    if suhu > 30:
        print ("Boleh keluar rumah, tapi pakai topi")
    else:
        print ("Gak boleh keluar rumah, nanti sakit")

elif cuaca == "berawan":
    if suhu < 30:
        print ("Boleh keluar rumah, tapi jaga-jaga kalau turun hujan")
    else:
        print ("Gak boleh keluar rumah")

elif cuaca == "Hujan":
    if suhu < 30:
        print ("Boleh pakai payung")
    else:
        print ("Gak boleh keluar rumah")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n ")

    
