# hello world

print ("Hello World")

print ("\n --- batas --- \n")




# variabel dasar

a = "Halo Dunia"
print ("A =", a)

b = "Halo Fun"
print ("B =", b)

c = 12
print ("C =", c)

d = 12.12
print ("D =", d)

e = True
print ("E =", e)


print ("\n --- batas --- \n")




# tipe data

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

fio = f"""
- Teks : {teks}
- Angka : {angka}
- Desimal : {desimal}
- Cek     : {cek}
"""

print (fio)


print ("\n --- batas --- \n")




# cek tipe data

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# fungsi dengan operasi dasar

x = int (input ("Masukkan angka a = "))
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


print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Bagi =", bagi (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# percabangan dasar

a = int (input ("Masukkan angka a = "))

if a >= 8:
    print (f"Besar, angka a = {a}")
    
else:
    print (f"Kecil, angka a = {a}")
    
    
print ("\n --- batas --- \n")




# percabangan lanjutan

b = int (input ("Masukkan angka b = "))

if b >= 8:
    print (f"Besar, angka b = {b}")
    
elif b >= 5:
    print (f"Sedang, angka b = {b}")
    
else:
    print (f"Kecil, angka b = {b}")
    
    
print ("\n --- batas --- \n")




# Percabangan nested

u = int (input ("Masukkan angka u = "))
cek = True

if u >= 8:
    if cek:
        print (f"besar, angka u = {u}")
        
    else:
        print (f"Sedang, angka u = {u}")
        
else:
    print (f"Kecil, angka u = {u}")
    

print ("\n --- batas --- \n")




# percabangan fungsi dasar

def ang (a):
    
    if a >= 8:
        print (f"Besar, angka a = {a}")
        
    else:
        print (f"kecil, angka a = {a}")
        
ang (10)
ang (9)
ang (8)
ang (7)
ang (6)
ang (5)
ang (4)
ang (3)
ang (2)
ang (1)


print ("\n --- batas --- \n")        



# fungsi dasar dengan percabangan lanjutan

def run (b):

    if b >= 8:
        print (f"Besar, angka b = {b}")

    elif b >= 5:
        print (f"kecil, angka b = {b}")

    else:
        print (f"Sedang, angka b = {b}")

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