print ("Hello World")

print ("\n --- batas --- \n")




# variabel dasar

a = "Halo Sore hari ini"
print (a)

b = "Halo untuk Kuliah Sore ini"
print (b)

c = "Halo Indonesia ku yang hebat"
print (c)

d = "Halo Gunship 1"
print (d)


print ("\n --- batas --- \n")




# Tipe data pemrograman

teks = "Halo Data 1"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
\n - Teks       : {teks}
\n - Angka      : {angka}
\n - Desimal    : {desimal}
\n - Cek        : {cek}
"""

print (tipe)

print ("\n --- batas --- \n")



# Fungsi dengan operasi dasar 

x = int (input ("Masukkan angka x : "))
y = int (input ("Masukkan angka y : "))

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