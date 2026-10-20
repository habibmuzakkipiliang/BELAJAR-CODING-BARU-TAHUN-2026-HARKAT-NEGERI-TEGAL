# Hello World

print ("Hello World")


print ("\n --- batas --- \n")



# Variabel

a = "Halo Dunia"
print (a)

b = "Halo Fun"
print (b)

c = 19
print (c)


d = True
print (d)


nama = "Habib Muzakki"
print (nama)


print ("\n --- batas --- \n")



jurusan = "D4 Vokasi Teknik Informatika"
print (jurusan)


print ("\n --- batas --- \n")



# Operator dasar

a = int (input ("Masukkan angka a : "))
b = int (input ("Masukkan angka b :"))

print ("Tambah =", a + b)
print ("Kurang =", a - b)
print ("Kali =", a * b)
print ("Bagi =", a / b)
print ("Pangkat =", a ** b)

print ("\n --- batas --- \n")



# Perbandingan

print ("Hasil =", a > b)
print ("Hasil =", a < b)
print ("Hasil =", a >= b)
print ("Hasil =", a <= b)
print ("Hasil =", a == b)
print ("Hasil =", a != b)

print ("\n --- batas --- \n")


# Logika

print ("Hasil =", a > b and a < b)
print ("Hasil =", a > b or a < b)
print ("Hasil =", not (a > b))
print ("Hasil =", not (a < b))


print ("\n --- batas --- \n")



# Percabangan dasar

nomor = int (input ("Masukkan nomor = "))

if nomor >= 8:
    print (f"Angka besar, nomor = {nomor}")

else:
    print (f"Angka kecil, nomor = {nomor}")


print ("\n --- batas --- \n")




# Percabangan lanjutan

angka = int (input ("Masukkan angka : "))

if angka >= 8:
    print (f"Angka besar, angka = {angka}")

elif angka >= 5:
    print (f"Angka sedang, angka = {angka}")

else:
    print (f"Angka kecil, angka = {nomor}")


print ("\n --- batas --- \n")



# Percabangan Nested

j = int (input ("Masukkan angka j = ?"))
cek = True

if j >= 8:
    if cek:
        print (f"Besar, angka j = {j}")

    else:
        print (f"Sedang, angka j = {j}")

else:
    print (f"Kecil, angka j = {j}")


print ("\n --- batas --- \n")




# Switch Case

nomor = 9

match (nomor):

    case 1:
        print (1)

    case 2:
        print (2)

    case 3:
        print (3)

    case 4:
        print (4)

    case _:
        print ("Semula")


print ("\n --- batas --- \n")




# Switch Case 1

hari = "Senin"

match (hari):

    case "Senin":
        print ("Senin")

    case "Selasa":
        print ("Selasa")

    case "Rabu":
        print ("Rabu")

    case "Kamis":
        print ("Kamis")

    case "Jumat":
        print ("Jumat")

    case _:
        print ("Libur")


print ("\n --- batas --- \n")



# For dasar

for a in range (1, 11):
    print (f"urutan ke - {a}")


print ("\n --- batas --- \n")



# For dasar 2

for i in range (1, 10):
    print (f"urutan ke - {i}")


print ("\n --- batas --- \n")



# For dasar 3

for y in range (1, 10):
    print (f"urutan ke - {y}")


print ("\n --- batas --- \n")




# For dasar 4

for h in range (1, 15):
    print (f"urutan ke - {h}")
    

print ("\n --- batas --- \n")