print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a)

b = 12
print ("B =", b)

c = 12.12
print ("C =", c)

d = True
print ("D =", d)

print ("\n --- batas --- \n")



# Switch Case

def run (a):

    match (a):

        case 1:
            print (1)

        case 2:
            print (2)

        case 3:
            print (3)

        case 4:
            print (4)

        case _:
            print ("semula")

run (1)
run (2)
run (3)
run (4)
run (5)
run (6)
run (7)
run (8)
run (9)
run (10)


print ("\n --- batas --- \n")



# Switch Case Lampu Lalu Lintas

def warna (k):

    match (k):

        case "Merah":
            print ("Warna merah")

        case "Kuning":
            print ("Warna kuning")

        case "Hijau":
            print ("Warna hijau")

        case _:
            print ("Warna lain")

warna ("Merah")
warna ("Kuning")
warna ("Hijau")
warna ("Hitam")

print ("\n --- batas ---- \n")



# Percabangan lanjutan

def rut (j):

    if j >= 8:
        print (f"besar, angka j = {j}")

    elif j >= 5:
        print (f"sedang, angka j = {j}")

    else:
        print (f"kecil, angka j = {j}")

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



# studi kasus warung nasi padang

f = """
====================================================

\t\t WARUNG NASI MILIK SAYA 

====================================================
"""

print (f)


nama_pemesan1 = str (input ("nama pemesan 1 = "))
nama_pemesan2 = str (input ("nama pemesan 2 = "))
nama_pemesan3 = str (input ("nama pemesan 3 = "))


nasi = 11000
telur_dadar = 11000
rendang = 15000
ayam_bakar = 17000
teh_tawar_panas = 13000
teh_es_manis = 12000


j_nasi = int (input ("berapa porsi nasi nya = "))
j_teh_tawar_panas = int (input ("berapa teh tawar panas nya = "))
j_tes_es_manis = int (input ("berapa teh es manis = "))
j_ayam_bakar = int (input ("berapa ayam bakar = "))
j_rendang = int (input ("berapa rendang nya = "))
j_telur_dadar = int (input ("berapa telur dadar nya = "))

uang_kamu = int (input ("berapa uang kamu = "))


a1 = j_ayam_bakar * ayam_bakar
a2 = j_nasi * nasi
a3 = j_teh_tawar_panas * teh_tawar_panas
a4 = j_tes_es_manis * teh_es_manis
a5 = j_rendang * rendang
a6 = j_telur_dadar * telur_dadar

total = a1 + a2 + a3 + a4 + a5 + a6 

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_uang = f"""
====================================================

\t\t RINCIAN DETAIL 

====================================================

- Nama pemesan 1    : {nama_pemesan1}
- Nama pemesan 2    : {nama_pemesan2}
- Nama pemesan 3    : {nama_pemesan3}
- Total biaya       : {total}
- Kembalian         : {kembalian}
- Cek               : {cek}

"""

print (rincian_uang)