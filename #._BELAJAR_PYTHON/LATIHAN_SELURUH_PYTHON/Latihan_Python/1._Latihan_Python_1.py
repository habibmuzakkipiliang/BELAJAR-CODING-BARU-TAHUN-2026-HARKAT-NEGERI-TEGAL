# Hello World

print ("Hello Dunia")
print ("Hello Fun")
print ("Hello Dun")


print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a)

b = 12
print ("B =", b)

c = 1.21
print ("C =", c)

d = True
print ("D =", d)

print ("\n --- batas --- \n")


# Input data

nama = input ("Siapa nama kamu ?")
print (nama)

asal = input ("Darimana kamu ?")
print (asal)

usia = int (input ("Usia kamu berapa ?"))
print (usia)

lengkap = f"Saya {nama} dari {asal} dan usia {usia}"
print (lengkap)

print ("\n --- batas --- \n")



# Biodata saya

nama = "Habib Muzakki"
asal = "Kota Serang, Bante"
jurusan = "D4 Teknik Informatika"
fakultas = "Vokasi"
tahun = "2026"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Vercel, Netlify, dan VS Code"

bio = f"""
- Nama     : {nama}
- Asal     : {asal}
- Jurusan  : {jurusan}
- Fakultas : {fakultas}
- Tahun    : {tahun}
- Coding   : {coding}
- Tools    : {tools}
"""

print (bio)

print ("\n --- batas --- \n")



# Tipe data 

teks = "Halo Teks"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
- Teks   : {teks}
- Angka  : {angka}
- Desimal : {desimal}
- Cek     : {cek}
"""

print (tipe)

print ("\n --- batas --- \n")



# Cek Tipe data

print (type (teks))
print (type (angka))
print (type (desimal))
print (type (cek))


print ("\n --- batas --- \n")



# Operator dasar

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

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Bagi =", bagi (x, y))
print ("Pangkat =", pangkat (x, y))


print ("\n --- batas --- \n")



# Operator perbandingan

print ("Hasil =", x > y)
print ("Hasil =", x < y)
print ("Hasil =", x >= y)
print ("Hasil =", x <= y)
print ("Hasil =", x == y)
print ("Hasil =", x != y)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar 1

def an (a):

    if a >= 8:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")

an (10)
an (7)
an (6)
an (5)
an (4)
an (3)
an (2)
an (1)


print ("\n --- batas --- \n")



# Percabangan Dasar 1

def nm (b):

    if b >= 7:
        print (f"Besar, angka b = {b}")

    else:
        print (f"Kecil, angka b = {b}")

nm (10)
nm (9)
nm (8)
nm (7)
nm (6)
nm (5)
nm (4)
nm (3)
nm (2)
nm (1)


print ("\n --- batas --- \n")




# Fungsi percabangan lanjutan

def ty (b):

    if b >= 8:
        print (f"Besar, angka b = {b}")

    elif b >= 5:
        print (f"Sedang, angka b = {b}")

    else:
        print (f"Kecil , angka b = {b}")


ty (10)
ty (9)
ty (8)
ty (7)
ty (6)
ty (5)
ty (4)


print ("\n --- batas --- \n")




# Percabangan nested 1

def gun (c):

    cek = True

    if c >= 8:
        if cek:
            print (f"Besar, angka c = {c}")

        else:
            print (f"Sedang, angka c = {c}")

    else:
        print (f"Kecil, angka c = {c}")

gun (10)
gun (8)
gun (7)
gun (4)
gun (3)
gun (2)
gun (1)


print ("\n --- batas --- \n")



# Percabangan nested 2

def ru (d):

    cek = True

    if d >= 8:
        if cek:
            print (f"Besar, angka d = {d}")

        elif d >= 5:
            print (f"Sedang, angka d = {d}")

    else:
        print (f"Kecil, angka d = {d}")

ru (10)
ru (9)
ru (8)
ru (7)
ru (6)
ru (5)
ru (4)
ru (3)
ru (2)
ru (1)


print ("\n --- batas --- \n")



# Percabangan lanjutan

def ru (f):

    if f >= 8:
        print (f"Besar, angka f = {f}")

    elif f >= 5:
        print (f"Sedang, angka f = {f}")

    else:
        print (f"Kecil, angka f = {f}")


ru (10)
ru (9) 
ru (5)
ru (3)
ru (2)
ru (1)
ru (6)
ru (8)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested 1

def der (g):

    cek = True

    if g >= 8:
        if cek:
            print (f"Besar, angka g = {g}")

        else:
            print (f"Sedang, angka j = {g}")

    else:
        print (f"Kecil, angka g = {g}")

der (10)
der (9)
der (8)
der (7)
der (6)
der (5)
der (4)
der (3)
der (2)
der (1)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan nested 2

def run (i):

    cek = True

    if i >= 8:
        if cek:
            print (f"Besar, angka i = {i}")

        elif i >= 5:
            print (f"Sedang, angka i = {i}")

    else:
        print (f"Kecil, angka i = {i}")

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




# Fungsi dengan percabangan nested 6

def run (i):

    cek = True

    if i >= 8:
        if cek:
            print (f"Besar, angka i = {i}")

        elif i >= 5:
            print (f"Sedang, angka i = {i}")

        else:
            print (f"Kecil, angka i = {i}")

    else:
        print (f"Kecil, angka i = {i}")

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