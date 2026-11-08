print ("Hello World")

print ("\n --- batas --- \n")


# Studi kasus warung kopi milik Nikson NTT

print ("""
==========================================================

STADI KASUS WARUNG KOPI MILIK NIKSON NTT

==========================================================
""")

kopi = 7000
kentang = 8000
aqua = 4000
popcorn = 4000
nasi_goreng = 8000
mie_ayam = 6000
mie_goreng = 7000

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))

j_kopi = int (input ("Masukkan kopi = "))
j_kentang = int (input ("Masukkan kentang = "))
j_aqua = int (input ("Masukkan aqua = "))
j_popcorn = int (input ("Masukkan popcorn = "))
j_nasi_goreng = int (input ("Masukkan nasi goreng = "))
j_mie_ayam = int (input ("Masukkan mie ayam = "))
j_mie_goreng = int (input ("Masukkan mie goreng sekarang = "))

a1 = j_kentang * kentang
a2 = j_aqua * aqua
a3 = j_kopi * kopi
a4 = j_popcorn * popcorn
a5 = j_mie_ayam * mie_ayam
a6 = j_nasi_goreng * nasi_goreng
a7 = j_mie_goreng * mie_goreng

total = a1 + a2 + a3 + a4 + a5 + a6 + a7

uang_kamu = int (input ("Masukkan uang kamu sekarang ini "))

kembalian_uang = uang_kamu - total

cek = uang_kamu > total


rincian_biaya = f"""
============================================================

RINCIAN PEMBAYARAN STUDI KASUS WARUNG KOPI MILIK NIKSON NTT

=========================================================

\n Nama pemesan 1       : {nama_pemesan1}
\n Nama pemesan 2       : {nama_pemesan2}
\n Nama pemesan 3       : {nama_pemesan3}
\n Total uang kamu      : {total}
\n Kembalian uang kamu  : {kembalian_uang}
\n Cek uang kamu        : {cek} 
"""

print (rincian_biaya)

print ("\n --- batas --- \n")



# studi kasus percabangan nonton bioskop dengan harga, genre, usia dan tempat bioskop nya

harga = int (input ("Masukkan harga sekarang = "))
genre = str (input ("Masukkan genre sekarang = "))
usia = int (input ("Masukkan usia kamu sekarang "))
tempat_bioskop = str (input ("Masukkan tampat bioskop sekarang = "))

if genre == "komedi":
    if usia >= 13 and usia <= 19:
        if tempat_bioskop == "mall":
            harga = 5000
            print ("Boleh nonton film sekarang")

        else:
            print ("Jangan nonton dulu")

elif genre == "romantis":
    if usia >= 18 and usia <= 25:
        if tempat_bioskop == "mal biasa":
            harga = 8000
            print ("Boleh nonton")

        else:
            print ("Jangan nonton dulu")

elif genre == "kartun":
    if usia >= 5 and usia <= 20:
        if tempat_bioskop == "cinepolis":
            harga = 9000
            print ("Boleh nonton kartun")

        else:
            print ("Jangan nonton dulu")

elif genre == "scifi robotik":
    if usia >= 19 and usia <= 30:
        if tempat_bioskop == "mall biasa":
            harga = 9000
            print ("Boleh nonton scifi robotik")

        else:
            print ("Jangan dulu ya bang")

elif genre == "robot perang":
    if usia >= 19 and usia <= 30:
        if tempat_bioskop == "mall besar":
            harga = 220000
            print ("Boleh nonton film itu")

        else:
            print ("Jangan nonton film itu dek")

elif genre == "perang dunia 1":
    if usia >= 20 and usia <= 40:
        if tempat_bioskop == "bioskop keren":
            harga = 30000
            print ("Boleh nonton sekarang")

        else:
            print ("Jangan nonton dulu ya dek")

elif genre == "perang dunia 2":
    if usia >= 20 and usia <= 45:
        if tempat_bioskop == "amerika serikat":
            harga = 7000
            print ("Boleh nonton film itu")

        else:
            print ("Jangan nonton ya dek")

elif genre == "thriller":
    if usia >= 20 and usia <= 45:
        if tempat_bioskop == "mall of serang":
            harga = 5000
            print ("Boleh nonton dong")

        else:
            print ("Jangan nonton dulu ya dek")

elif genre == "jkt48":
    if usia >= 13 and usia <= 20:
        if tempat_bioskop == "fx sudirman":
            harga = 90000
            print ("Boleh nonton sekarang di Fx Sudirman")

        else:
            print ("Harus ditemani orang dewasa untuk nonton itu")

else:
    print ("Input tidak valid")


akhir_data = f"""
- Kamu pilih genre film {genre}, dengan harga Rp {harga}, tempat bioskop {tempat_bioskop}

"""

print (akhir_data)


print ("\n --- batas --- \n")



# Studi kasus percabangan prakiraan cuaca hari ini 

cuaca = str (input ("Masukkan cuaca hari ini (berawan, hujan dan cerah) = "))
suhu = int (input ("Masukkan suhu hari ini dalam celcius = "))

if cuaca == "cerah":
    if suhu > 30:
        print ("Cerah dan boleh berangkat ke luar rumah")

    else:
        print ("Jangan keluar rumah dulu")

elif cuaca == "berawan":
    if suhu < 30:
        print ("Bisa jalan-jalan ke rumah sekarang ini")

    else:
        print ("Jangan keluar rumah dulu")

elif cuaca == "hujan":
    if suhu < 30:
        print ("Bawa payung, dan cuaca nya dingin")

    else:
        print ("Jangan keluar rumah dulu")


else:
    print ("Input tidak valid")


cuaca = f"""
- Cuaca hari ini {cuaca} dengan suhu {suhu} celcius
"""
print (cuaca)

print ("\n --- batas --- \n")




# Studi kasus tentang percabangan pemilihan sepatu 

jenis_sepatu = str (input ("Masukkan jenis sepatu sekarang = "))
harga_sepatu = int (input ("Masukkan harga sepatu = "))

if jenis_sepatu == "mahal super":
    if harga_sepatu >= 100000 and harga_sepatu <= 500000:
        print ("Mahal")

    else:
        print ("Jangan beli sepatu dong")

elif jenis_sepatu == "mahal":
    if harga_sepatu >= 50000 and harga_sepatu <= 100000:
        print ("Boleh beli sepatu jika mampu")

    else:
        print ("Jangan beli sepatu dong")

elif jenis_sepatu == "menengah atas":
    if harga_sepatu >= 40000 and harga_sepatu <= 70000:
        print ("Boleh sepatu jika mampu")

    else:
        print ("Jangan beli sepatu dulu")

elif jenis_sepatu == "menengah ke bawah":
    if harga_sepatu >= 20000 and harga_sepatu <= 40000:
        print ("Boleh beli sepatu")

    else:
        print ("Jangan beli sepatu")

elif jenis_sepatu == "murah biasa":
    if harga_sepatu >= 10000 and harga_sepatu <= 30000:
        print ("Boleh beli lah")

    else:
        print ("Jangan beli sepatu dong")

elif jenis_sepatu == "murah meriah":
    if harga_sepatu >= 5000 and harga_sepatu <= 10000:
        print ("Boleh aja")

    else:
        print ("Pilih sepatu lain")

else:
    print ("Input tidak valid")


data_akhir = f"""
- Kamu pilih jenis sepatu {jenis_sepatu} dengan harga Rp {harga_sepatu}
"""

print (data_akhir)

print ("\n --- batas --- \n")


# Studi kasus tentang percabangan pemilihan Handphone

jenis_hp = str (input ("Masukkan jenis status hp = "))
usia_kamu = int (input ("Masukkan usia kamu = "))
harga_hp = int (input ("Masukkan harga hp sekarang = "))

if jenis_hp == "mahal":
    if harga_hp >= 10000000:
        if usia_kamu >= 13 and usia <= 20:
            print ("Kamu boleh beli hp itu")

        else:
            print ("Jangan kamu beli hp nya")

elif jenis_hp == "mid menengah atas":
    if harga_hp >= 6000000:
        if usia_kamu >= 13 and usia <= 20:
            print ("Berarti kamu boleh memiliki nya")

        else:
            print ("Jangan kamu beli")

elif jenis_hp == "mid menengah kebawah":
    if harga_hp >= 3000000:
        if usia_kamu >= 13 and usia <= 20:
            print ("Maka kamu boleh memiliki nya")

        else:
            print ("Jangan kamu beli hp nya")

elif jenis_hp == "murah":
    if harga_hp >= 1000000:
        if usia_kamu >= 13 and usia <= 20:
            print ("Boleh kamu memiliki nya")

        else:
            print ("Jangan kamu beli hp nya")

else:
    print ("Input tidak valid")


akhir = f"""
- Kamu memiliki HP {jenis_hp} dengan harga {harga_hp} dan usia kamu sekarang {usia_kamu} tahun
"""

print (akhir)


print ("\n --- batas --- \n")


# Studi kasus percabangan pemilihan laptop

harga_laptop = int (input ("Masukkan harga laptop = "))
jenis_laptop = str (input ("Masukkan jenis laptop = "))
usia_anda = int (input ("Masukkan usia anda = "))

if jenis_laptop == "mahal":
    if harga_laptop >= 15000000:
        if usia_anda >= 15 and usia <= 20:
            print ("Kamu boleh memiliki laptop mahal itu")

        else:
            print ("Jangan kamu memiliki nya")

elif jenis_laptop == "menengah":
    if harga_laptop >= 5000000:
        if usia_anda >= 15 and usia <= 20:
            print ("Boleh anda memiliki laptop menengah")

        else:
            print ("Jangan kamu memiliki nya")

elif jenis_laptop == "murah":
    if harga_laptop >= 3000000:
        if usia_anda >= 15 and usia_anda <= 20:
            print ("Kamu boleh memiliki nya dong")

        else:
            print ("Jangan kamu memiliki nya")

else:
    print ("Input tidak valid")


data_terakhir = f"""
- Kamu memiliki Laptop {jenis_laptop} dengan harga laptop Rp {harga_laptop} dengan usia anda {usia_anda} tahun
"""

print (data_terakhir)

print ("\n --- batas --- \n")