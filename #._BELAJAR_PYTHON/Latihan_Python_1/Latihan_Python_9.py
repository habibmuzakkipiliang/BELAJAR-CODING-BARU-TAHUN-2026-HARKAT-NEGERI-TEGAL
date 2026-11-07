# Hello World

print ("Hello World")

print ("\n --- batas --- \n")




# variabel

a = "Halo Dunia"
print ("A =", a)

b = 12
print ("B =", b)

c = True
print ("C =", c)


print ("\n --- batas --- \n")



# Tipe data pemrograman

teks = "Halo UHN Tegal"
angka = 12
desimal = 12.12
cek = True

tipe = f"""
- Teks      : {teks}
- Angka     : {angka}
- Desimal   : {desimal}
- Cek       : {cek}

"""

print (tipe)


print ("\n --- batas --- \n")




# Cek tipe data pemrograman

print ("Teks =", type (teks))
print ("Angka =", type (angka))
print ("Desimal =", type (desimal))
print ("Cek =", type (cek))


print ("\n --- batas --- \n")



# Studi kasus Kopi Bahagia milik Nikson NTT

toko = """
=====================================================================================

\t\t Studi Kasus Kopi Bahagia Milik Nikson NTT

====================================================================================
"""

print (toko)


print ("\n --- batas --- \n")




kopi = 5000
teh_manis_anget = 4000
teh_es_manis = 5000
nasi = 4000
aqua = 2000
kentang = 5000


j_kentang = int (input ("berapa buah kentang nya = "))
j_nasi = int (input ("berapa nasi nya = "))
j_aqua = int (input ("berapa aqua nya = "))
j_teh_manis_anget = int (input ("berapa teh manis anget nya = "))
j_teh_es_manis = int (input ("berapa teh es manis = "))
j_kopi = int (input ("berapa kopi nya = "))

a1 = j_aqua * aqua
a2 = j_kentang * kentang
a3 = j_kopi * kopi
a4 = j_nasi * nasi
a5 = j_teh_es_manis * j_teh_es_manis
a6 = j_teh_manis_anget * teh_manis_anget

total = a1 + a2 + a3 + a4 + a6 

uang_kamu = int (input ("berapa uang kamu = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_biaya = f"""
- Total biaya seluruh nya   : {total}
- Uang kamu                 : {uang_kamu}
- Kembalian uang            : {kembalian}
- Cek                       : {cek}

"""

print (rincian_biaya)

print ("\n --- batas --- \n")