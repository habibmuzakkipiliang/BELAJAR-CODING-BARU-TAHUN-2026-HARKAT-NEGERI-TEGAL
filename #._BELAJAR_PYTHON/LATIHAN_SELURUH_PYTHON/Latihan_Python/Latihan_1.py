# tes pertama

print ("Hello World")


print ("\n --- batas --- \n")



# Variabel

angka = 12
print ("Angka =", angka) 

desimal = 12.12
print ("Desimal =", desimal)

teks = "Halo Dunia"
print ("Teks =", teks)

cek = True
print ("Cek =", cek)


print ("\n --- batas --- \n")



# Operator dasar

a = int (input ("Masukkan angka a = "))
b = int (input ("Masukkan angka b = "))

def tambah (a, b):
    return a + b

def kurang (a, b):
    return a - b

def kali (a, b):
    return a * b

def pangkat (a, b):
    return a ** b

def bagi (a, b):
    return a / b


print ("Tambah =", tambah (a, b))
print ("Kurang =", kurang (a, b))
print ("Kali =", kali (a, b))
print ("Bagi =", bagi (a, b))
print ("Pangkat =", pangkat (a, b))


print ("\n --- batas --- \n")



# Operator perbandingan

print ("Hasil =", a > b)
print ("Hasil =", a < b)
print ("Hasil =", a >= b)
print ("Hasil =", a <= b)
print ("Hasil =", a == b)
print ("Hasil =", a != b)


print ("\n --- batas --- \n")



# Logika 

print ("Hasil =", a < b and a > b)
print ("Hasil =", a > b or a < b)
print ("Hasil =", not (a > b))
print ("Hasil =", not (a < b))