# input data nama orang

nama = input ("Masukkan nama kamu = ")
print ("Nama kamu adalah =", nama)


print ("\n --- batas --- \n")



# input data nama, usia, asal, dan tinggi badan

nama = input ("Masukkan nama kamu = ")
usia = int (input ("Masukkan usia kamu = "))
asal = input ("Masukkan asal daerah kamu = ")
tinggi = int (input ("Masukkan tinggi badan kamu = "))


bio = f"""
- Nama      : {nama}
- Usia      : {usia}
- Asal      : {asal}
- Tinggi    : {tinggi}

"""

print (bio)

print ("\n --- batas --- \n")



# input data lengkap

nama = input ("Masukkan nama kamu = ")
asal = input ("Masukkan asal daerah kamu = ")
usia = int (input ("Masukkan usia kamu = "))
tinggi = float (input ("Masukkan tinggi badan kamu ="))
berat = float (input ("Masukkan berat badan kamu = "))


hun = f"""
- Nama              : {nama}
- Asal              : {asal}
- Usia              : {usia}
- Tinggi badan      : {tinggi}
- Berat badan       : {berat}
"""

print (hun)

print ("\n --- batas --- \n")



# Input nama kamu dan pekerjaan kamu

nama = input ("Masukkan nama kamu = ")
kerja = input ("Masukkan kerja kamu = ")

hi = f"""
- Nama         : {nama}
- Kerja        : {kerja}
"""

print (hi)

print ("\n --- batas --- \n")



# Input nama dan perkenalan

nama = input ("Masukkan nama kamu = ")
usia = int (input ("Masukkan usia kamu = "))
kerja = input ("Masukkan kerja kamu = ")

yun = f"""
- Nama      : {nama}
- Usia      : {usia}
- Kerja     : {kerja}
"""

print (yun)

print ("\n --- batas --- \n")


 
# input login dan password

username = input ("Masukkan username kamu = ")
password = input ("Masukkan password kamu = ")

if username == "@habib_muzakki":
    print ("Tepat")

else:
    print ("Belum tepat")


print ("\n --- batas --- \n")


if password == "123":
    print ("Tepat")

else:
    print ("Belum tepat")


print ("\n --- batas --- \n")