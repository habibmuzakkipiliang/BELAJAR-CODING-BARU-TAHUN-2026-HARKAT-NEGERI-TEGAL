print ("Selamat datang di Latihan Python")


print ("\n --- batas --- \n")



# biodata pribadi

nama = "Habib Muzakki"
asal = "Kota Serang, Banten"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel dan Netlify"
hobi = "Ngewota JKT48 dan Suka Oshi JKT48 + Denger Musik"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
kampus = "Universitas Harkat Negeri Tegal"



bio = f"""
- Nama lengkap  : {nama}
- Asal          : {asal}
- Coding        : {coding}
- Tools         : {tools}
- Hobi          : {hobi}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Universitas   : {kampus}

"""

print (bio)

print ("\n --- batas --- \n")




# Studi kasus Kafe milik Nikson

fg = """
====================================================

\t\t KAFE BAHAGIA MILIK NIKSON

====================================================
"""

print (fg)


kopi = 3000
kentang = 5000
es_teh = 3000
teh_anget = 5000
botol_minum = 4000
nasi = 5000
ayam_bakar = 7000
ayam_goreng = 6000
burger = 5000

nama_pemesan1 = str (input ("nama pemesan 1 = "))
nama_pemesan2 = str (input ("nama pemesan 2 = "))
nama_pemesan3 = str (input ("nama pemesan 3 = "))

j_ayam_bakar = int (input ("berapa ayam bakar = "))
j_ayam_goreng = int (input ("berapa ayam goreng = "))
j_burger = int (input ("berapa burger nya = "))
j_nasi = int (input ("berapa porsi nasi nya = "))
j_botol_minum = int (input ("berapa botol minum nya = "))
j_kopi = int (input ("berapa kopi nya = "))
j_es_teh = int (input ("berapa es teh nya = "))
j_teh_anget = int (input ("berapa teh anget nya = "))


a1 = j_ayam_bakar * ayam_bakar
a2 = j_ayam_goreng * ayam_goreng
a3 = j_botol_minum * botol_minum
a4 = j_burger * burger 
a5 = j_kopi * kopi
a6 = j_teh_anget * teh_anget
a7 = j_es_teh * es_teh

uang_kamu = int (input ("berapa uang kamu = "))

total = a1 + a2 + a3 + a4 + a5 + a6 + a7

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian = f"""
- Nama pemesan 1    : {nama_pemesan1}
- Nama pemesan 2    : {nama_pemesan2}
- Nama pemesan 3    : {nama_pemesan3}
- Total uang        : {total}
- Kembalian         : {kembalian}
- Cek               : {cek}

"""

print (rincian)


print ("\n --- batas --- \n")


# Switch Case

r = int (input ("berapa angka random = "))

def ruty (r):

    match (r):

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

ruty (r)
ruty (r)
ruty (r)
ruty (r)
ruty (r)
ruty (r)
ruty (r)
ruty (r)


print ("\n --- batas --- \n")


# Pemilihan warna dalam switch case

o = str (input ("masukkan warna = "))

def rut (o):

    match (o):

        case "Merah":
            print ("Merah")

        case "Kuning":
            print ("Kuning")

        case "Hijau":
            print ("Hijau")

        case _:
            print ("Semula")

rut (o)
rut (o)
rut (o)
rut (o)
rut (o)
rut (o)
rut (o)
rut (o)


print ("\n --- batas --- \n")



# Fungsi dengan percabangan dasar

r = int (input ("berapa angka random = "))

def ruk (r):

    if r >= 5:
        print (f"besar, angka r = {r}")

    else:
        print (f"kecil, angka r = {r}")

ruk (r)
ruk (r)
ruk (r)
ruk (r)
ruk (r)
ruk (r)
ruk (r)
ruk (r)


print ("\n --- batas --- \n")




# Fungsi dengan percabangan lanjutan 

a = int (input ("berapa angka random kamu = "))

def run (a):

    if a >= 8:
        print (f"besar, angka a = {a}")

    elif a >= 5:
        print (f"sedang, angka a = {a}")

    else:
        print (f"kecil, angka a = {a}")

run (a)
run (a)
run (a)
run (a)
run (a)
run (a)
run (a)
run (a)
run (a)
run (a)


print ("\n --- batas --- \n")



# Nested 1 

b = int (input ("berapa angka random = "))

def rut (b):

    cek = True

    if b >= 8:
        if cek:
            print (f"besar, angka b = {b}")

        else:
            print (f"sedang, angka b = {b}")

    else:
        print (f"kecil, angka b = {b}")

rut (b)
rut (b)
rut (b)
rut (b)
rut (b)
rut (b)
rut (b)
rut (b)
rut (b)


print ("\n --- batas --- \n")



# Nested 2

t = int (input ("berapa angka random = "))

def tu (t):

    cek = True

    if t >= 6:
        if cek:
            print (f"besar, angka t = {t}")

        elif t >= 5:
            print (f"sedang, angka t = {t}")

    else:
        print (f"kecil, angka t = {t}")

tu (t)
tu (t)
tu (t)
tu (t)
tu (t)
tu (t)
tu (t)
tu (t)


print ("\n --- batas --- \n")



# Usia masuk JKT48 dan Join nya

k = int (input ("berapa usia gabung ke JKT48 nya = "))

def jkt48 (k):

    if k >= 15 and k <= 20:
        print (f"boleh join jkt48 sekarang juga, usia = {k}")

    elif k > 20:
        print (f"usia yang lebih dari cukup, usia = {k}")

    else:
        print (f"kecil, angka k = {k}")

jkt48 (k)
jkt48 (k)
jkt48 (k)
jkt48 (k)
jkt48 (k)
jkt48 (k)
jkt48 (k)
jkt48 (k)


print ("\n --- batas --- \n")



# Usia produktif manusia 

h = int (input ("berapa usia produktif manusia = "))

def run (h):

    if h >= 15 and h <= 45:
        print (f"masuk usia produktif, usia = {h}")

    elif h > 45:
        print (f"usia yang sudah tua, usia = {h}")

    else:
        print (f"usia yang masih kecil, usia = {h}")

run (h)
run (h)
run (h)
run (h)
run (h)
run (h)
run (h)
run (h)


print ("\n --- batas --- \n")



# Usia masuk kuliah 

y = int (input ("berapa usia masuk kuliah = "))

def usia (y):

    if y >= 19 and y < 25:
        print (f"boleh masuk kuliah, usia = {y}")

    elif y > 25:
        print (f"usia yang sudah lebih dari cukup, usia = {y}")

    else:
        print (f"usia yang belum boleh, usia = {y}")

usia (y)
usia (y)
usia (y)
usia (y)
usia (y)
usia (y)
usia (y)
usia (y)
usia (y)
usia (y)


print ("\n --- batas --- \n")


# Fungsi dengan mencari angka terbesar

t = int (input ("masukkan angka t = "))
k = int (input ("masukkan angka k = "))

def angka_besar (t, k):

    if t > k:
        return k 

    else:
        return t

print ("Hasil =", angka_besar (t, k))
print ("Hasil =", angka_besar (t, k))
print ("Hasil =", angka_besar (t, k))


print ("\n --- batas --- \n")


for i in range (1, 20):
    print (f"urutan ke - {i}")

for a in range (11):
    print (f"urutan ke - {a}")

for j in range (1, 20):
    print (f"urutan ke - {j}")


print ("\n --- batas --- \n")


print ("Daftar Oshi JKT48 saya")

oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Michie JKT48", "Fritzy JKT48", "Lana JKT48"]

oshi.append ("Lana JKT48")
oshi.append ("Erine JKT48")
oshi.append ("Anindya JKT48")
oshi.append ("Freya JKT48")

for r in oshi:
    print (r)


print ("\n --- batas --- \n")