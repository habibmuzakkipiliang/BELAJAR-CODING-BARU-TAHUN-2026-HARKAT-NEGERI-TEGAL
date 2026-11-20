# hello world

print ("hello world")


print ("\n --- batas --- \n")


# variabel dasar

a = "Halo Dunia"
print ("a =", a)

b = "Halo Fun"
print ("b =", b)

c = 19
print ("c =", c)

d = True
print ("D =", d)

print ("\n --- batas --- \n")



# Fungsi dasar dengan operator dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def kali (x, y):
    return x * y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))

print ("\n --- batas --- \n")


# Cek tipe data

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

cek = f"""
- Teks      : {teks}
- Angka     : {angka}
- Desimal   : {desimal}
- Cek       : {cek}
"""

print (cek)

print ("\n --- batas --- \n")



# Cek tui