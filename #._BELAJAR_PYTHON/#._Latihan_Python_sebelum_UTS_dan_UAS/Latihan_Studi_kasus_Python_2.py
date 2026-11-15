print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Hello World"
print (a)

b = "Halo Dunia ku"
print (b)

c = 132
print (c)

d = True
print (d)


print ("\n --- batas --- \n")


# Studi kasus pemilihan usia manusia asli

usia = input ("Masukkan usia kamu = ")
status_p = ()


if usia >= 1 and usia <= 2:
    status_p = "bayi"
    print ("bayi")

elif usia >= 2 and usia <= 4:
    status_p = "balita"
    print ("balita")

elif usia >= 5 and usia <= 7:
    status_p = "Anak-anak"
    print ("Anak-anak")

elif usia >= 7 and usia <= 12:
    status_p = "Pra Remaja"
    print ("Pra remaja")

elif usia >= 13 and usia <= 20:
    status_p = "Remaja"
    print ("Remaja")

elif usia >= 20 and usia <= 30:
    status_p = "Dewasa"
    print ("Dewasa")

elif usia >= 30 and usia <= 45:
    status_p = "Orang tua"
    print ("Orang tua")

elif usia >= 45 and usia <= 70:
    status_p = "Lanjut usia"
    print ("Lanjut usia")

else:
    print ("Input tidak valid")


manusia = f"""
usia kamu = {usia} dengan status = {status_p} dan selamat data kamu sudah terinput dengan sangat baik
"""

print (manusia)


print ("\n --- batas --- \n")


# Studi kasus pemilihan jenjang pendidikan kamu

usia_pendidikan = input ("Masukkan usia jenjang pendidikan kamu = ")
jenjang = input ("Masukkan jenjang kamu = ")
status_1 = ()

if jenjang == "tk":
    if usia_pendidikan >= 3 and usia <= 6:
        status_1 = "TK"
        print ("Sudah TK")

    else:
        print ("Jangan dulu ya")

elif jenjang == "sd":
    if usia_pendidikan >= 6 and usia <= 13:
        status = "SD"
        print ("Masuk sd")

    else:
        print ("Masih tk")

elif jenjang == "smp":
    if usia_pendidikan >= 13 and usia <= 16:
        status_1 = "SMP"
        print ("Sudah masuk smp")

    else:
        print ("masih smp")

elif jenjang == "sma":
    if usia_pendidikan >= 16 and usia <= 19:
        status_1 = "SMA"
        print ("Sudah masuk SMA")

    else:
        print ("Masih smp")

elif jenjang == "kuliah":
    if usia_pendidikan >= 19 and usia <= 27:
        status_1 = "Kuliah"
        print ("Sudah masuk kuliah")

    else:
        print ("Masih SMA")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")


pendidikan = f"""

jenjang kamu adalah {jenjang} dengan usia {usia_pendidikan}

selamat data kamu sudah terinput dengan baik dan benar

"""

print (pendidikan)

print ("\n --- batas --- \n")



# Studi kasus pemilihan genre film dan usia

usia = input ("Masukkan usia kamu dong = ")
genre_film =  input ("Masukkan genre film dong = ")

if genre_film == "horor":
    if usia >= 18 and usia <= 25:
        harga_film = 5000
        print ("Boleh nonton film horor")

    else:
        print ("Jangan dulu ya dek")

elif genre_film == "komedi":
    if usia >= 13 and usia <= 23:
        harga_film = 5000
        print ("Boleh nonton komedi")

    else:
        print ("Jangan dulu ya")

elif genre_film == "romantis":
    if usia >= 18 and usia <= 25:
        harga_film = 6000
        print ("Boleh nonton romantis")

    else:
        print ("Jangan dulu ya dek")

elif genre_film == "animasi":
    if usia >= 10 and usia <= 20:
        harga_film = 8000
        print ("Boleh nonton")

    else:
        print ("Jangan dulu ya")

else:
    print ("Input tidak valid")


rincian_detail = f"""
Kamu nonton = {genre_film} dan usia kamu sekarang = {usia} dengan harga = {harga_film}
"""

print (rincian_detail)


print ("\n --- batas --- \n")



