# Hello World

print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a)



# Operator dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x - y

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



# Tipe data 

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

fio =  f"""
- Teks      : {teks}
- Angka     : {angka}
- Desimal   : {desimal}
- Cek       : {cek}
"""

print (fio)


print ("\n --- batas --- \n")




# cek tipe data 

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# percabangan dasar

a = 6

if a >= 8:
    print (f"Besar, angka a = {a}")

else:
    print (f"Kecil, angka a = {a}")


print ("\n --- batas --- \n")



# Percabangan lanjutan

b = 7

if b >= 8:
    print (f"besar, angka b = {b}")

elif b >= 5:
    print (f"sedang, angka b = {b}")

else:
    print (f"kecil, angka b = {b}")


print ("\n --- batas --- \n")



# percabangan nested 1

g = 7
cek = True

if g >= 8:
    if cek:
        print (f"besar, angka g = {g}")

    else:
        print (f"sedang, angka g = {g}")

else:
    print (f"kecil, angka g = {g}")


print ("\n --- batas --- \n")




# Percabangan nested 2

y = 8
cek = True

if y >= 8:
    if cek:
        print (f"besar, angka y = {y}")

    elif y >= 5:
        print (f"sedang, angka y = {y}")

else:
    print (f"kecil, angka y = {y}")


print ("\n --- batas --- \n")



# Struktur data (Array) dasar

dat = ["Halo Dunia", "Halo Indonesia", "Halo Tegal", "Halo Jatim"]

for i in dat:
    print (i)


print ("\n --- batas --- \n")



# buah-buahan

buah = ["Mangga", "Apel", "Melon", "Semangka", "Pepaya", "Manggis", "Anggur"]

buah.append ("Buah Merah")
buah.append ("Buah Naga")
buah.append ("Buah Zaitun")
buah.append ("Buah Aneh")

for h in buah:
    print (h)

print ("\n --- batas --- \n")



# Struktur data Dict

data = {
    "nama" : "Habib Muzakki",
    "asal" : "Kota Serang", 
    "coding" : "HTML, CSS, JavaScript dan Python", 
    "tools" : "Github, Github Pages, Vercel, Netlify, Search Console",
}

print ("Nama :", data ["nama"])
print ("Asal :", data ["asal"])
print ("Coding :", data ["coding"])
print ("Tools :", data ["tools"])


print ("\n --- batas --- \n")



# Fungsi dasar

def dasar ():
    print ("Hello World")

dasar ()


print ("\n --- batas --- \n")



# Fungsi dengan parameter

def halo (nama):
    return f"Halo nama saya {nama} dari Kota Serang"

halo ("Rayyan")
halo ("Fayyan")
halo ("Yun")


print ("\n --- batas --- \n")