print ("Hello World")

print ("\n --- batas --- \n")



# variabel dasar

a = "Helo Dunia"
print (a)

b = "Hai Dunia"
print (b)

c = "Fan"
print (c)

d = True
print (d)


print ("\n --- batas --- \n")



# Studi kasus tentang toko kopi milik Kak Isko NTT Flores

print ("""
============================================================

Studi kasus tentang cafe  milik Kak Isko NTT Flores

=============================================================

""")

kopi = 4000
kentang = 4000
nasi_goreng = 8000
mie_goreng = 5000
mie_ayam = 6000
bakso = 7000

j_bakso = int (input ("Masukkan bakso = "))
j_mie_ayam = int (input ("Masukkan mie ayam = "))
j_mie_goreng = int (input ("Masukkan mie goreng = "))
j_nasi_goreng = int (input ("Masukkan nasi goreng = "))
j_kentang = int (input ("Masukkan kentang = "))
j_kopi = int (input ("Masukkan kopi = "))


a1 = j_bakso * bakso
a2 = j_kentang * kentang
a3 = j_kopi * kopi
a4 = j_mie_ayam * mie_ayam
a5 = j_nasi_goreng * nasi_goreng
a6 = j_mie_goreng * mie_goreng

total = a1 + a2 + a3 + a4 + a5 + a6 

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_pembayaran = f"""
===================================================

RINCIAN PEMBAYARAN

===================================================

\n Total uang       : {total}
\n Kembalian        : {kembalian}
\n Uang kamu        : {uang_kamu}
\n Cek              : {cek}


"""

print (rincian_pembayaran)


print ("\n --- batas --- \n")




# Skor 

skor = int (input ("Masukkan skor kamu = "))

if skor >= 90:
    print (f"Skor A,  skor = {skor}")

elif skor >= 80:
    print (f"Skor B, skor = {skor}")

elif skor >= 70:
    print (f"Skor C, skor = {skor}")

elif skor >= 60:
    print (f"Skor D, skor = {skor}")

elif skor >= 50:
    print (f"Skor E, skor = {skor}")

elif skor >= 40:
    print (f"Skor F, skor = {skor}")

else:
    print (f"Skor tidak valid, skor = {skor}")


print ("\n --- batas --- \n")