# tes awal

print ("hai Gracie JKT48")
print ("Hai Lily JKT48")
print ("Hai Aralie JKT48")

print ("\n --- batas --- \n")




# tipe data 

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
- Teks : {teks}
- Angka : {angka}
- Desimal : {desimal}
- Cek : {cek}
"""

print (tipe)

print ("\n --- batas --- \n")



# cek tipe data

print ("Teks :", type (teks))
print ("Angka :", type (angka))
print ("Desimal :", type (desimal))
print ("Cek :", type (cek))


print ("\n --- batas --- \n")




# fungsi dasar dengan operasi dasar

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



# Perkenalan input nama dan usia

nama = input ("Masukkan nama kamu = ")
usia = int (input ("Masukkan usia kamu ="))

print ("Halo nama saya ", nama, "Dari Jakarta Timur ", "Usia saya ", usia)


print ("\n --- batas --- \n")




# perkenalan nama, usia, asal, tinggi badan

nama = input ("Masukkan nama kamu = ")
usia = int (input ("Masukkan usia kamu = "))
asal = input ("Masukkan asal kamu =")
tinggi = int (input ("Masukkan tinggi badan ="))


profil = f"""
- Nama         : {nama}
- Usia         : {usia}
- Asal         : {asal}
- Tinggi badan : {tinggi}
"""

print (profil)

print ("\n --- batas --- \n")




# percabangan dasar

a = int (input ("Masukkan angka a = "))

if a >= 8:
    print (f"besar, angka a = {a}")

else:
    print (f"kecil, angka a = {a}")

print ("\n --- batas --- \n")



# percabangan lanjutan 

e = int (input ("Masukkan angka e = "))

if e >= 8:
    print (f"besar, angka e = {e}")

elif e >= 5:
    print (f"sedang, angka e = {e}")

else:
    print (f"kecil, angka e = {e}")


print ("\n --- batas --- \n")



