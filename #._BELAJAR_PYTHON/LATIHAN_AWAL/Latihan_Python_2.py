# hello world

print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a)

b = 12.12
print ("B =", b)

c = True
print ("C =", c)

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
desimal = 13.12
cek = True

rio = f"""
- Teks      : {teks}
- Angka     : {angka}
- Desimal   : {desimal} 
- Cek       : {cek}

"""

print (rio)

print ("\n --- batas --- \n")



# Cek tipe data

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar

def ang (a):

    if a >= 5:
        print (f"Besar, angka a = {a}")

    else:
        print (f"Kecil, angka a = {a}")

ang (10)
ang (9)
ang (7)
ang (5)
ang (4)
ang (3)
ang (2)
ang (1)


print ("\n --- batas --- \n")




# percabangan lanjutan

def un (b):

    if b >= 8:
        print (f"besar, angka b = {b}")

    elif b >= 5:
        print (f"sedang, angka b = {b}")

    else:
        print (f"kecil, angka b = {b}")

un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (1)


print ("\n --- batas --- \n")



# percabangan nested dalam fungsi

def run (d):

    cek = True

    if d >= 8:
        if cek:
            print (f"besar, angka d = {d}")

        else:
            print (f"sedang, angka d = {d}")

    else:
        print (f"kecil, angka d = {d}")

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




# Percabangan dasar

a = 9

if a >= 5:
    print (f"besar, angka a = {a}")

else:
    print (f"kecil, angka a = {a}")


print ("\n --- batas --- \n")




# percabangan lanjutan

b = 4

if b >= 8:
    print (f"besar, angka b = {b}")

elif b >= 5:
    print (f"sedang, angka b = {b}")

else:
    print (f"Kecil, angka b = {b}")


print ("\n --- batas --- \n")



# percabangan nested 

e = 3
cek = True

if e >= 8:
    if cek:
        print (f"besar, angka e = {e}")

    else:
        print (f"sedang, angka e = {e}")

else:
    print (f"kecil, angka e = {e}")


print ("\n --- batas --- \n")




# percabangan nested 1

r = 8
cek = True

if r >= 8:
    if cek:
        print (f"besar, angka r = {r}")

    elif r >= 5:
        print (f"sedang, angka r = {r}")

else:
    print (f"kecil, angka r = {r}")


print ("\n --- batas --- \n")



# Array 

tu = ["apel", "pir", "semangka", "melon", "pepaya", "lengkeng"]

tu.append ("naga")
tu.append ("buah merah papua")
tu.append ("salak")
tu.append ("sawo")


for u in tu:
    print (u)


print ("\n --- batas --- \n")