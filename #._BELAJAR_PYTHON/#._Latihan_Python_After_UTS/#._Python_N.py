print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print (a)

b = 12
print (b)

c = 12.2
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# tipe data pemrograman

teks = "Halo Dunia"
angka = 12
desimal = 12.2
cek = True

tipe = f"""
\n Teks     : {teks}
\n Angka    : {angka}
\n Desimal  : {desimal}
\n Cek      : {cek}


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

angka_2 = int (input ("Masukkan angka = "))

if angka_2 > 0:
    print (f"Angka positif, angka = {angka_2}")

else:
    print (f"Angka negatif, angka = {angka_2}")


print ("\n --- batas --- \n")



# Percabangan lanjutan

angka_3 = int (input ("Masukkan angka = "))

if angka_3 > 0:
    print (f"Angka positif, angka = {angka_3}")

elif angka_3 < 0:
    print (f"Angka negatif, angka = {angka_3}")

else:
    print (f"Angka nol, angka = {angka_3}")


print ("\n --- batas --- \n")



# Percabangan Nested 

angka = int (input ("Masukkan angka = "))

if angka > 0:
    if cek:
        print (f"Angka positif, angka = {angka}")

    elif angka < 0:
        print (f"Angka negatif, angka = {angka}")

else:
    print (f"Angka nol, angka = {angka}")

print ("\n --- batas --- \n")