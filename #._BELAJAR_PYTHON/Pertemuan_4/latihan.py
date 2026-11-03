# Hello World

print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

a = "Hello World"
print ("A =", a)

b = 12
print ("B =", b)

c = 12.123
print ("C =", c)

e = True
print ("E =", e)


print ("\n --- batas --- \n")



# Fungsi dengan operasi dasar

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

def bagi (x, y):
    return x / y

def modulus (x, y):
    return x % y

def bagi_bulat (x, y):
    return x // y


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))
print ("Bagi bulat =", bagi_bulat (x, y))
print ("Bagi =", bagi (x, y))


print ("\n --- batas --- \n")



# Operator dasar

a = int (input ("Masukkan angka a = "))
b = int (input ("Masukkan angka b = "))

print ("Tambah =", a + b)
print ("Kurang =", a - b)
print ("Kali =", a * b)
print ("Pangkat =", a ** b)
print ("Modulus =", a % b)
print ("Bagi bulat =", a // b)
print ("Bagi =", a / b)


print ("\n --- batas --- \n")




# Fungsi variasi operator

r = int (input ("Masukkan angka r = "))
u = int (input ("Masukkan angka u = "))
i = int (input ("Masukkan angka i = "))

def tambah (r, u, i):
    return r + u + i

def kurang (r, u, i):
    return r - u - i

def kali (r, u, i):
    return r * u * i

def pangkat (r, u, i):
    return r ** u ** i

def bagi_bulat (r, u, i):
    return r // u // i


print ("Tambah =", tambah (r, u, i))
print ("Kurang =", kurang (r, u, i))
print ("Kali =", kali (r, u, i))
print ("Pangkat =", pangkat (r, u, i))
print ("Bagi bulat =", bagi_bulat (r, u, i))


print ("\n --- batas --- \n")




# Fungsi dengan return percabangan dasar

def run (h):
    if h >= 8:
        print (f"besar, angka h = {h}")

    else:
        print (f"kecil, angka h = {h}")

run (10)
run (9)
run (8)
run (5)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")



# latihan dasar

a = int (input ("Masukkan angka pertama = "))
b = int (input ("Masukkan angka kedua = ")) 

hasil = a + b
print ("Tambah =", hasil)


print ("\n --- batas --- \n")




# Error Handling

try:
    a = 10 / 0
    print (a)

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Berhasil")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")



# Raise Error Handling

def ru (u):

    try:

        if u < 0:
            raise ("gagal")

        if u >= 8:
            print (f"besar, angka u = {u}")

        elif u >= 5:
            print (f"sedang, angka u = {u}")

        else:
            print (f"kecil, angka u = {u}")

    except:
        print (f"angka gak boleh minus, angka u = {u}")

ru (10)
ru (9)
ru (8)
ru (4)
ru (-12)
ru (-34)
ru (-45)
ru (-56)
ru (-67)
ru (-89)


print ("\n --- batas --- \n")




# Raise Error Handling

def ri (k):

    try:

        if k < 0:
            raise ("Minus")

        if k >= 5:
            print (f"besar, angka k = {k}")

        else:
            print (f"kecil, angka k = {k}")

    except:
        print (f"Angka gak boleh minus, angka u = {k}")


ri (-19)
ri (-34)
ri (-45)
ri (10)
ri (8)
ri (3)
ri (2)
ri (1)


print ("\n --- batas --- \n")





# barang-barang