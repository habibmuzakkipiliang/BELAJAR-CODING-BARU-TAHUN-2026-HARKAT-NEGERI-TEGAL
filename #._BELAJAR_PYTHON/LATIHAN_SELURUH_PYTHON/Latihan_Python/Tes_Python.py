# hello world

print ("Hello World")

print ("\n --- batas --- \n")




# variabel dasar

alap = "John Jon"
print ("Alap =", alap)

a = "Halo Dunia"
print ("A =", a)

b = 12
print ("B =", b)


print ("\n --- batas --- \n")




# biodata Ramon Salazar

nama = "Ramon Salazar"
asal = "Spanyol"
julukan = "Bocil Kematian"
usia = 20
sekutu = "Osmund Saddler, Bitores Mendez, Jack Krauser"
organisasi = "Los Iluminados"
musuh = "Leon S. Kennedy, Ada Wong, Chris Redfield"


bio = f"""
- Nama : {nama}
- Asal : {asal}
- Julukan : {julukan}
- Usia : {usia}
- Sekutu : {sekutu}
- Organisasi : {organisasi}
- Musuh : {musuh}

"""


print (bio)


print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

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

print ("Hasil penjumlahan x + y =", tambah (x, y))
print ("Hasil pengurangan x - y =", kurang (x, y))  
print ("Hasil perkalian x * y =", kali (x, y))
print ("Hasil perpangkatan x ** y =", pangkat (x, y))


print ("\n --- batas --- \n") 





# list 

gun = ["Api", "Air", "Angin", "Bumi", "Petir"]

gun.append ("Cahaya")
gun.append ("Kegelapan")
gun.append ("Es")
gun.append ("Racun")
gun.append ("Baja")

for i in gun:
    print (i)


print ("\n --- batas --- \n")