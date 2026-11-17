# Hello World

print ("Hello World")


print ("\n --- batas --- \n")



# variabel

a = "Helo Dunia"
print ("A =", a)

b = "Halo Fer"
print ("B =", b)

c = 19
print ("C =", c)

d = True
print ("D =", d)


print ("\n --- batas --- \n")



# Operasi dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x * y

def bagi (x, y):
    return x / y

def pangkat (x, y):
    return x ** y

def modulus (x, y):
    return x % y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Bagi =", bagi (x, y))
print ("Pangkat =", pangkat (x,  y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Operator perbandingan

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- batas --- \n")



# Operasi Logika

print ("Hasil =", x > y and x > y)
print ("Hasil =", x < y or x > y)
print ("Hasil =", not (x > y))
print ("Hasil =", not (x < y))


print ("\n --- batas --- \n")



# Percabangan dasar

a = 8

if a >= 5:
    print (f"Besar, angka a = {a}")

else:
    print (f"Kecil, angka a = {a}")


print ("\n --- batas --- \n")




# Percabangan lanjutan

b = 4

if b >= 8:
    print (f"Besar, angka b = {b}")

elif b >= 5:
    print (f"Sedang, angka b = {b}") 

else:
    print (f"Kecil, angka b = {b}")


print ("\n --- batas --- \n")



# Percabangan nested 9

k = 8 
cek = True

if k >= 8:
    if cek:
        print (f"Besar, angka k = {k}")

    else:
        print (f"Sedang, angka k = {k}")

else:
    print (f"Kecil, angka k = {k}")


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar

def run (a):

    if a >= 5:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)


print ("\n --- batas --- \n")




# Array 1

der = [
    "Minecraft",
    "RE 3"
    "RE 2",
    "RE 1",
    "RE 5",
    "RE 7",
    "Basara Heroes 2",
    "Gunship Battle",

]

der.append ("Mobil")
der.append ("Sam")
der.append ("Gur")
der.append ("Lop")
der.append ("Guan Ping")
der.append ("Guan Yu")
der.append ("Yan Baihu")

for h in der:
    print (h)


print ("\n --- batas --- \n")



# Array 3

fer = [
    "Gracie",
    "Aralie",
    "Lily",
    "Michie"
    "Fritzy",
    "Lana",
    "Erine",
    "Delynn",
]

fer.append ("Anindya")
fer.append ("Freya")
fer.append ("Olla")
fer.append ("Eli")
fer.append ("Mikaela")
fer.append ("Ekin")
fer.append ("Intan")
fer.append ("Trisha")


for k in fer:
    print (k)


print ("\n --- batas --- \n")