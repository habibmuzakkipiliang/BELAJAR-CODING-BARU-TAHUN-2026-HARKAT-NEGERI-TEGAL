# hello world

print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a) 

b = "Halo Olla JKT48"
print ("B =", b) 

c = 12
print ("C =", c)

d = 3.12
print ("D =", d)


print ("\n --- batas --- \n")



# fungsi dengan operasi dasar

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

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))


print ("\n --- batas --- \n")



# Operator 

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- batas --- \n")



# Array 
 
li = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48"]

li.append ("Lana JKT48")
li.append ("Erine JKT48")
li.append ("Delynn JKT48")
li.append ("Anindya JKT48")
li.append ("Freya JKT48")
li.append ("Olla JKT48")
li.append ("Christy JKT48")


for u in li:
    print (u)


print ("\n --- batas --- \n")



# Struktur

data = {
    "nama" : "Habib Muzakki",
    "kelas" : "1B",
    "jurusan" : "D4 Teknik Informatika",
    "asal" : "Kota Serang",
    "coding" : "HTML, CSS, JavaScript dan Python",
}

print ("Nama :", data ["nama"])
print ("Kelas :", data ["kelas"])
print ("Asal :", data ["asal"])
print ("Coding :", data ["coding"])


print ("\n --- batas --- \n")



# fungsi dasar

def dasar ():
    print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dasar dengan parameter

def nama (halo):
    print (f"Halo nama saya {halo} dari Kota Serang, Banten")

nama ("Habib")
nama ("Hayyan")
nama ("Rayyan")
nama ("Fayyan")
nama ("Onnican")


print ("\n --- batas --- \n")



# Fungsi dengan return

def run (nama):
    return f"Halo nama saya {nama} dari Jakarta Timur"

print (run ("Habib"))
print (run ("Rayyan"))
print (run ("Gracie JKT48"))
print (run ("Lily JKT48"))
print (run ("Fritzy JKT48"))
print (run ("Michie JKT48"))

print ("\n --- batas --- \n")