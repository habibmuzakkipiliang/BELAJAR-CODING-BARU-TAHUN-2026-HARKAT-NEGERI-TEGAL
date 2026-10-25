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




# Studi kasus nonton bioskop

nama_film = [
    "Cinnepolis",
    "XXI",
    "Gajah Mada",
    "CGV"
]

for i in nama_film:
    print (i)


nama_bioskop = str (input ("nama bioskop nya = "))


print ("\n --- batas --- \n")


genre = [
    "Horor",
    "Romantis",
    "Thriller",
    "Sci Fi",
    "Action",
]

for j in genre:
    print (j)


nama_genre = str (input ("apa nama genre film yang kamu inginkan = "))


print ("\n --- batas --- \n")


on = """
- Popcorn   : Rp 30.000
- Aqua      : Rp 30.000
- Tiket     : Rp 25.000

"""

print (on)


popcorn = 30000
aqua = 30000
tiket = 25000


j_popcorn = int (input ("berapa popcorn nya = "))
j_aqua = int (input ("berapa aqua nya = "))
j_tiket = int (input ("berapa tiket nya = "))


nama_pemesan1 = str (input ("nama pemesan 1 = "))
nama_pemesan2 = str (input ("nama pemesan 2 = "))
nama_pemesan3 = str (input ("nama pemesan 3 = "))


a1 = j_aqua * aqua
a2 = j_popcorn * popcorn
a3 = j_tiket * tiket


total = a1 + a2 + a3

uang_kamu = int (input ("berapa uang kamu sekarang = "))

kembalian_uang = uang_kamu - total

cek = uang_kamu > total


rincian_biaya = f"""
- Nama pemesan 1    : {nama_pemesan1}
- Nama pemesan 2    : {nama_pemesan2}
- Nama pemesan 3    : {nama_pemesan3}
- Total uang        : {total}
- Kembalian         : {kembalian_uang}
- Cek               : {cek}
"""

print (rincian_biaya)


print ("\n --- batas --- \n")