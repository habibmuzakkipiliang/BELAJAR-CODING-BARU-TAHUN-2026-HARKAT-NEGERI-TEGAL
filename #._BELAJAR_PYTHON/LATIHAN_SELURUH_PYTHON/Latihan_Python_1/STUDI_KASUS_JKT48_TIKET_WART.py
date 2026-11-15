print ("Hello World")


print ("\n --- batas --- \n")



# variabel dasar

a = "Halo Dunia"
print ("A =", a)

print ("\n --- batas --- ")



# Fungsi dengan percabangan dasar

def run (a):

    if a >= 8:
        print (f"besar, angka a = {a}")

    elif a >= 5:
        print (f"sedang, angka a = {a}")

    else:
        print (f"kecil, angka a = {a}")

run (10)
run (9)
run (8)
run (1)
run (4)
run (5)
run (6)


print ("\n --- batas --- \n")



# Fungsi dengan switch case int 

def rut (j):

    match (j):

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

        case 6:
            print (6)

        case _:
            print ("Semula")

rut (1)
rut (2)
rut (3)
rut (4)
rut (5)
rut (6)
rut (7)


print ("\n --- batas --- \n")


def angka_besar (r, t):

    if r > t:
        return r

    else:
        return t


print ("Angka besar =", angka_besar (10, 2))
print ("Angka besar =", angka_besar (4, 20))
print ("Angka besar =", angka_besar (50, 3))
print ("Angka besar =", angka_besar (4, 30))


print ("\n --- batas --- \n")


# Fungsi mencari angka terkecil

def angka_kecil (a, b):

    if a < b:
        return a

    else:
        return b

print ("Angka kecil = ", angka_kecil (10, 8))
print ("Angka kecil = ", angka_kecil (10, 3))
print ("Angka kecil = ", angka_kecil (2, 29))
print ("Angka kecil =", angka_kecil (30, 3))


print ("\n --- batas --- \n")



# Studi kasus tentang tiket JKT48

masuk_parkir = 2000
meet_and_greet = 25000
two_shoot = 20000
handshake = 19000
tiket_jkt48 = 20000

nama_pemesan1 = str (input ("nama pemesan 1 = "))
nama_pemesan2 = str (input ("nama pemesan 2 = "))
nama_pemesan3 = str (input ("nama pemesan 3 = "))


J_tiket_jkt48 = int (input ("berapa buah tiket jkt48 = "))
j_meet_and_greet = int (input ("berapa tiket meet and greet jkt48 = "))
j_two_shoot = int (input ("berapa tiket two shoot jkt48 = "))
j_handshake = int (input ("berapa tiket handshake jkt48 = "))
j_masuk_parkir = int (input ("berapa tiket parkir nya = "))


a1 = j_handshake * handshake
a2 = j_masuk_parkir * masuk_parkir
a3 = j_meet_and_greet * meet_and_greet
a4 = j_two_shoot * two_shoot
a5 = J_tiket_jkt48 * tiket_jkt48

total = a1 + a2 + a3 + a4 + a5

uang_kamu = int (input ("berapa uang kamu sekarang = "))

kembalian = uang_kamu - total

cek = uang_kamu > total


rincian_biaya = f"""
============================================================================

\t\t RINCIAN BIAYA TIKET JKT48 DAN SAMBIL NGEWOTA JKT48

============================================================================
\n - Nama pemesan 1     : {nama_pemesan1}
\n - Nama pemesan 2     : {nama_pemesan2}
\n - Nama pemesan 3     : {nama_pemesan3}
\n - Total biaya        : {total}
\n - Kembalian uang     : {kembalian}
\n - Cek                : {cek}
"""

print (rincian_biaya)

print ("\n --- batas --- \n")