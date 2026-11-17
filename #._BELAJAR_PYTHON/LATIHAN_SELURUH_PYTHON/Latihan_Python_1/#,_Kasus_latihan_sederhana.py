# Hello World

print ("Hello World")

print ("\n --- batas --- \n")



# Biodata pribadi saya

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
kampus = "Universitas Harkat Negeri Tegal"
semester = 1
domisili = "Kota Tegal, Jawa Tengah"
hobi = "Ngewota JKT48 + suka denger musik JKT48 + suka dengan member jkt48 yang cantik-cantik"



bio = f"""
======================================================================================

\t\t\t BIODATA HABIB MUZAKKI LENGKAP 

======================================================================================

- Nama      :   {nama}
- Asal      :   {asal}
- Jurusan   :   {jurusan}
- Fakultas  :   {fakultas}
- Kampus    :   {kampus}
- Semester  :   {semester}
- Domisili  :   {domisili}
- Hobi      :   {hobi}

"""

print (bio)

print ("\n --- batas --- \n")



print ("""
=====================================================================================

\t\t\t Daftar Oshi JKT48 (List + Method List Python)

======================================================================================

""")

oshi = [
    "Gracie JKT48",
    "Aralie JKT48",
    "Lily JKT48",
    "Michie JKT48",
    "Freya JKT48",
]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Delynn JKT48")
oshi.append ("Oline JKT48")
oshi.append ("Freya JKT48")
oshi.append ("Anindya JKT48")
oshi.append ("Trisha JKT48")
oshi.append ("Christy JKT48")
oshi.append ("Olla JKT48")
oshi.append ("Jessi JKT48")
oshi.append ("Fiony JKT48")
oshi.append ("Muthe JKT48")
oshi.append ("Marsha JKT48")
oshi.append ("Eli JKT48")
oshi.append ("Celine Eks JKT48")
oshi.append ("Jemima JKT48")
oshi.append ("Mikaela JKT48")
oshi.append ("Ekin JKT48")
oshi.append ("Intan JKT48")

for n in oshi:
    print (n)

print ("\n --- batas --- \n")



print ("""
======================================================================================

\t\t\t\t Variabel dasar

======================================================================================

""")

a = "Halo Dunia"
print ("A =", a)

b = 12
print ("B =",b)

c = 12.12
print ("C =", c)

d = True
print ("D =", d)


print ("\n --- batas --- \n")



print ("""
======================================================================================

\t\t\t Tipe data pemrograman 

======================================================================================

""")

teks = "Halo Dunia"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
- Teks      :   {teks}
- Angka     :   {angka}
- Desimal   :   {desimal}
- Cek       :   {cek}
"""

print (tipe)


print ("\n --- batas --- \n")



print ("""
=====================================================================================

\t\t\t Cek Tipe Data Pemrograman 

=====================================================================================

""")

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Studi kasus tentang warung nasi padang

fio = """
======================================================================================

\t\t\t Studi Kasus tentang warung Nasi padang

======================================================================================

"""

print (fio)

nasi = 5000
ayam_bakar = 6000
ayam_goreng = 7000
ayam_ijo = 6000
daging_rendang = 7000
daging_gulai = 8000
daging_ayam = 9000
ayam_gulai = 7000

nama_pemesan1 = str (input ("nama pemesan 1 = "))
nama_pemesan2 = str (input ("nama pemesan 2 = "))
nama_pemesan3 = str (input ("nama pemesan 3 = "))

j_ayam_gulai = int (input ("berapa ayam gulai = "))
j_nasi = int (input ("berapa porsi nasi nya = "))
j_daging_ayam = int (input ("berapa daging ayam nya = "))
j_daging_gulai = int (input ("berapa daging gulai nya = "))
j_daging_rendang = int (input ("berapa daging rendang nya = "))
j_ayam_ijo = int (input ("berapa ayam ijo nya = "))
j_ayam_bakar = int (input ("berapa ayam bakar nya = "))


a1 = j_ayam_bakar * ayam_bakar
a2 = j_ayam_gulai * ayam_gulai
a3 = j_daging_ayam * daging_ayam
a4 = j_ayam_ijo * ayam_ijo
a5 = j_daging_ayam * daging_ayam
a6 = j_daging_rendang * daging_rendang
a7 = j_nasi * nasi
a8 = j_daging_gulai * daging_gulai

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 

uang_kamu = int (input ("berapa uang kamu = "))

kembalian = uang_kamu - total

print ("\n --- batas --- \n")




rincian_biaya = f"""
======================================================================================

\t\t\t Rincian biaya keselurahan nya di Warung Nasi Padang 

======================================================================================

- Nama pemesan 1    :   {nama_pemesan1}
- Nama pemesan 2    :   {nama_pemesan2}
- Nama pemesan 3    :   {nama_pemesan3}
- Total biaya       :   {total}
- Uang kamu         :   {uang_kamu}
- Kembalian         :   {kembalian}
- Cek               :   {cek}
"""

print (rincian_biaya)

print ("\n --- batas --- \n")



# Fungsi dengan operator dasar

x = 9
y = 5

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


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

def run (a):

    if a >= 5:
        print (f"besar, angka a = {a}")

    else:
        print (f"kecil, angka a = {a}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (2)
run (3)
run (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan lanjutan

def rut (t):

    if t >= 8:
        print (f"besar, angka t = {t}")

    elif t >= 5:
        print (f"sedang, angka t = {t}")

    else:
        print (f"kecil, angka t = {t}")

rut (10)
rut (9)
rut (8)
rut (7)
rut (6)
rut (5)
rut (4)
rut (3)
rut (2)
rut (1)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan nested

def rut (i):

    cek = True

    if i >= 8:
        if cek:
            print (f"besar, angka i = {i}")

        else:
            print (f"sedang, angka i = {i}")

    else:
        print (f"kecil, angka i = {i}")

rut (10)
rut (9)
rut (8)
rut (7)
rut (6)
rut (5)
rut (4)
rut (3)
rut (2)
rut (1)


print ("\n --- batas --- \n")



# Switch Case

def ruy (d):

    match (d):

        case 1:
            print (1)

        case 2:
            print (2)

        case 3:
            print (3)

        case 4:
            print (4)

        case 5:
            print (5)

        case _:
            print ("Semula")

ruy (1)
ruy (2)
ruy (3)
ruy (4)
ruy (5)
ruy (6)
ruy (7)


print ("\n --- batas --- \n")



# Switch Case String

def ryu (e):

    match (e):

        case "Merah":
            print ("Warna merah")

        case "Kuning":
            print ("Warna kuning")

        case "Hijau":
            print ("Warna hijau")

        case _:
            print ("Semula")

ryu ("Merah")
ryu ("Kuning")
ryu ("Hijau")
ryu ("Hitam")


print ("\n --- batas --- \n")



# Fungsi dengan mencari angka terbesar

def angka_besar (x, y):

    if x > y:
        return x 

    else:
        return y

print ("Angka besar =", angka_besar (10, 3))
print ("Angka besar =", angka_besar (3, 20))
print ("Angka besar =", angka_besar (8, 90))
print ("Angka besar =", angka_besar (7, 30))


print ("\n --- batas --- \n")



# Fungsi dengan mencari angka terkecil

def angka_kecil (a, b):

    if a < b:
        return a

    else:
        return b

print ("Angka kecil =", angka_kecil (3, 12))
print ("Angka kecil =", angka_kecil (5, 89))
print ("Angka kecil =", angka_kecil (9, 50))
print ("Angka kecil =", angka_kecil (4, 90))
print ("Angka kecil =", angka_kecil (9, 20))


print ("\n --- batas --- \n")



# For dasar
 
for i in range (1, 20):
    print (f"urutan ke - {i}")

for r in range (5, 10):
    print (f"urutan ke - {r}")

for h in range (20, 40):
    print (f"urutan ke - {h}")


print ("\n --- batas --- \n")



# While dasar 

a = 1

while a < 10:
    print (f"urutan ke - {a}")
    a = a + 1


b = 10
while b > 0:
    print (f"urutan ke - {b}")
    b = b - 1


print ("\n --- batas --- \n")



# Error Handling

try:
    a = 10 + 10

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")




# Error Handling 

try:
    f = 10 / 0

except ZeroDivisionError:
    print ("Gagal")

else:
    print ("Oke")

finally:
    print ("Selesai")


print ("\n --- batas --- \n")



# Fungsi dengan Raise Error Handling

def rui (i):

    try:

        if i < 0:
            raise ("Gagal")

        if i >= 5:
            print (f"besar, angka i = {i}")

        else:
            print (f"kecil, angka i = {i}")

    except:
        print (f"Gak boleh angka minus, angka i = {i}")

rui (10)
rui (9)
rui (8)
rui (7)
rui (5)
rui (3)
rui (2)
rui (1)


print ("\n --- batas --- \n")



# Fungsi dengan raise Error Handling

def un (t):

    try:

        if t < 0:
            raise ("Gagal")

        if t >= 8:
            print (f"besar, angka t = {t}")

        elif t >= 5:
            print (f"sedang, angka t = {t}")

        else:
            print (f"kecil, angka t = {t}")

    except:
        print (f"Gak boleh minus, angka t = {t}")


un (10)
un (9)
un (8)
un (7)
un (6)
un (5)
un (4)
un (3)
un (2)
un (1)


print ("\n --- batas --- \n")



print ("""
======================================================================================

\t\t\t DICTIONARY 

======================================================================================

""")

data = {
    "nama" : "Habib Muzakki",
    "asal" : "Kota Serang",
    "umur" : 19,
    "golongan_darah" : "B",
    "hobi" : "JKT48",
}

print ("Nama =", data ["nama"])
print ("Asal =", data ["asal"])
print ("Umur =", data ["umur"])
print ("Golongan darah =", data ["golongan_darah"])
print ("Hobi =", data ["hobi"])


print ("\n --- batas --- \n")