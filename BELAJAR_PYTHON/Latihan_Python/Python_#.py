# Hello World

print ("Hello World")


print ("\n --- batas --- \n")




# variabel

a = "Halo Dunia"
print ("A =", a)

b = "Halo Indonesia"
print ("B =", b)

c = 12
print ("C =", c)

d = True
print ("D =", d)


print ("\n --- batas --- \n")




# Operator dasar

x = int (input ("Masukkan angka x ="))
y = int (input ("Masukkan angka y ="))

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




# Operasi perbandingan

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- batas --- \n") 




# Operasi logika

print ("Hasil =", x < y and x > y)
print ("Hasil =", x > y or x < y)
print ("Hasil =", not (x > y))
print ("Hasil =", not (x < y))


print ("\n --- batas --- \n")



# Fungsi dasar dengan percabangan dasar

def un (a):

    if a >= 5:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


print ("\n --- batas --- \n")




# Fungsi dasar dengan percabangan lanjutan

def ju (b):

    if b >= 8:
        print (f"Besar, angka b = {b}")

    elif b >= 5:
        print (f"Sedang, angka b = {b}")

    else:
        print (f"Kecil, angka b = {b}")

ju (10)
ju (9)
ju (8)
ju (7)
ju (6)
ju (5)
ju (4)
ju (3)
ju (2)
ju (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested

def df (h):

    cek = True

    if h >= 8:
        if cek:
            print (f"Besar, angka h = {h}")

        else:
            print (f"Sedang, angka h = {h}")

    else:
        print (f"Kecil, angka h = {h}")

df (10)
df (9)
df (8)
df (7)
df (6)
df (5)
df (4)
df (3)
df (2)
df (1)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan nested

def ij (g):

    cek = True

    if g >= 8:
        if cek:
            print (f"Besar, angka g = {g}")

        elif g >= 5:
            print (f"Sedang, angka g = {g}")

    else:
        print (f"Kecil, angka g = {g}")

ij (10)
ij (9)
ij (8)
ij (4)
ij (2)
ij (1)


print ("\n --- batas --- \n")