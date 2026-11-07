print ("Hello World")


print ("\n --- batas --- \n")



# Biodata lengkap Habib Muzakki

nama_lengkap = "Habib Muzakki"
nama_panggilan = "Habib"
asal_daerah = "Kota Serang"
nim = 26090040 
coding = "HTML, CSS, JavaScript dan Python"
hobi_saya = "JKT48, main game offline dan suka denger musik"
kampus = "Universitas Harkat Negeri Tegal"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
kelas = "1B"


biodata_lengkap = f"""
\n Nama lengkap     : {nama_lengkap}
\n Nama panggilan   : {nama_panggilan}
\n Asal daerah      : {asal_daerah}
\n NIM              : {nim}
\n Coding           : {coding}
\n Hobi saya        : {hobi_saya}
\n Kampus kuliah    : {kampus}
\n Jurusan          : {jurusan}
\n Fakultas         : {fakultas}

"""

print (biodata_lengkap)

print ("\n --- batas --- \n")



# variabel dasar

a = "Hello World"
print (a)

b = "Halo Dunia ku"
print (b)

c = 12
print (c)


print ("\n --- batas --- \n")



# Fungsi return dengan operator dasar

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
    return x + y

def kurang (x, y):
    return x - y

def pangkat (x, y):
    return x ** y

def modulus (x, y):
    return x % y

def kali (x, y):
    return x * y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Pangkat =", pangkat (x, y))
print ("Modulus =", modulus (x, y))


print ("\n --- batas --- \n")



# Rumus Luas bangun datar yang lengkap

s = int (input ("Masukkan sisi nya = "))
p = int (input ("Masukkan panjang nya = "))
l = int (input ("Masukkan lebar nya = "))
phi = 3.14
r = int (input ("Masukkan jari-jari lingkaran = "))
a = int (input ("Masukkan alas segitiga = "))
t = int (input ("Masukkan tinggi segitiga = "))
d1 = int (input ("Masukkan d1 layang - layang = "))
d2 = int (input ("Masukkan d2 layang - layang = "))

def luas_persegi (s):
    return s * s

def luas_persegi_panjang (p, l):
    return p * l

def luas_lingkaran (phi, r):
    return phi * r * r

def luas_segitiga (a, t):
    return a * t / 2

def luas_layang_layang (d1, d2):
    return d1 * d2 / 2

print ("Luas persegi =", luas_persegi (s, s))
print ("Luas persegi panjang =", luas_persegi_panjang (p, l))
print ("Luas segitiga =", luas_segitiga (a, t))
print ("Luas lingkaran =", luas_lingkaran (phi, r))
print ("Luas layang-layang =", luas_layang_layang (d1, d2))


print ("\n --- batas --- \n")





# Percabangan usia produktif manusia saat ini 

usia_sekarang = int (input ("Masukkan usia saat ini = "))
cek = True

if usia_sekarang >= 15 and usia_sekarang <= 45:
    if cek:
        print (f"Sudah masuk usia produktif, usia {usia_sekarang}")

    elif usia_sekarang > 45:
        print (f"usia anda sudah tua, usia = {usia_sekarang}")

else:
    print (f"Usia belum produktif, usia = {usia_sekarang}")

print ("\n --- batas --- \n")




# Studi kasus pemilihan jenis laptop 

jenis_laptop = input ("Masukkan jenis laptop kamu = ")

if jenis_laptop == "Gaming berat":
    print (f"Laptop kamu jenis {jenis_laptop}")

elif jenis_laptop == "gaming ringan":
    print (f"Jenis laptop kamu {jenis_laptop}")

elif jenis_laptop == "kuliah":
    print (f"jenis laptop kamu adalah {jenis_laptop}")

elif jenis_laptop == "tingkat menengah":
    print (f"Jenis laptop kamu adalah {jenis_laptop}")

elif jenis_laptop == "tingkat rendah":
    print (f"Jenis laptop kamu adalah {jenis_laptop}")

else:
    print (f"Input tidak valid {jenis_laptop}")


print ("\n --- batas --- \n")