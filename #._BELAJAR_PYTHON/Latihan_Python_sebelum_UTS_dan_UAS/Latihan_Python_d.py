print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print (a)

b = 12
print (b)

c = True
print (c)

print ("\n --- batas --- \n")



# Studi kasus tentang percabangan nilai skor 

skor = int (input ("Masukkan skor nya dong = "))

if skor >= 90:
    print (f"A, nilai = {skor}")

elif skor >= 80:
    print (f"B, nilai = {skor}")

elif skor >= 70:
    print (f"C, nilai = {skor}")

else:
    print (f"Input tidak valid, nilai = {skor}")


print ("\n --- batas --- \n")




# Studi kasus percabangan dasar

fun = int (input ("Masukkan percabangan dasar = "))

if fun >= 8:
    print (f"Sudah nilai = {fun}")

else:
    print (f"Belum nilai {fun}")


print ("\n --- batas --- \n")




# Studi kasus tentang percabangan lanjut

usia = int (input ("Masukkan usia kamu berap = "))

if usia >= 15 and usia <= 45:
    print (f"Sudah masuk usia produktif, usia = {usia}")

elif usia > 45:
    print (f"Sudah tua, usia = {usia}")

else:
    print (f"Masih kecil, usia = {usia}")


print ("\n --- batas --- \n")




# Status fungsi dengan dasar

def dasar ():
    print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Status percabangan nested

usia_jkt48 = int (input ("Masukkan usia jkt48 = "))
cek = True

if usia_jkt48 >= 10 and usia_jkt48 <= 19:
    if cek:
        print (f"Sudah masuk usia yang oke, usia = {usia_jkt48}")

    elif usia_jkt48 > 19:
        print (f"Sudah tua, usia = {usia_jkt48}")

else:
    print (f"Masih kecil usia kamu, usia = {usia_jkt48}")


print ("\n --- batas --- \n")




# Studi kasus percabangan kompleks 

jenis_jenjang = str (input ("Masukkan jenjang = "))
usia = int (input ("Masukkan usia kamu = "))
cek = True

if jenis_jenjang == "sd":
    if usia >= 13 and usia <= 19:
        if cek:
            print (f"Jenjang = {jenis_jenjang} dan usia = {usia}")

        else:
            print (f"Jenjang = {jenis_jenjang} dan usia = {usia} ")

elif jenis_jenjang == "smp":
    if usia >= 13 and usia <= 19:
        print (f"Jenjang = {jenis_jenjang} dan usia = {usia}")

    else:
        print (f"Jenjang = {jenis_jenjang} dan usia = {usia}")

elif jenis_jenjang == "sma":
    if usia >= 13 and usia <= 19:
        print (f"Jenjang = {jenis_jenjang} dan usia = {usia}")

    else:
        print (f"Jenjang = {jenis_jenjang} dan usia = {usia}")

elif jenis_jenjang == "kuliah":
    if usia >= 13 and usia <= 19:
        print (f"Sudah kuliah = {jenis_jenjang} dan usia = {usia}")

    else:
        print (f"Sudah {jenis_jenjang} dan usia {usia}")

else:
    print (f"Input tidak valid, jenjang = {jenis_jenjang} dan usia = {usia}")


print ("\n --- batas --- \n")