# Hello World

print ("Hello World")


print ("\n --- batas --- \n")




# variabel dasar

a = "Halo dunia"
print ("A =", a)

b = 10
print ("B =", b)

c = 12.2
print ("C =", c)

d = True
print ("D =", d)


print ("\n --- batas --- \n")



teks = "Halo dunia"
print (teks)

print (type (teks))


angka = 12
print (angka)

print (type (angka))



# operasi dasar

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