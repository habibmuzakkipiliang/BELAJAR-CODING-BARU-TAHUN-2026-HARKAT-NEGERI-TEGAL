print ("Hello World")

print ("\n --- batas --- \n")


# Studi kasus pemilihan buku 

pilih_buku = input ("Masukkan buku apa kamu mau pilih = ")

if pilih_buku == "komik":
    harga_buku = 5000
    print ("Pilihan kamu komik")

elif pilih_buku == "novel":
    harga_buku = 4000
    print ("Pilihan kamu novel")

elif pilih_buku == "buku mapel":
    harga_buku = 6000
    print ("Pilihan kamu buku mapel")

elif pilih_buku == "buku masak":
    harga_buku = 6000
    print ("Pilihan kamu buku masak")

elif pilih_buku == "buku panduan elektronik":
    harga_buku = 7000
    print ("Pilihan kamu buku panduan elektronik")

elif pilih_buku == "buku coding":
    harga_buku = 8000
    print ("Pilihan kamu buku coding")

else:
    print ("Input tidak valid")


fop = f"Buku pilihan kamu = {pilih_buku} dan dengan harga = {harga_buku}"

print (fop)


uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

total_harga = harga_buku

kembalian = uang_kamu - total_harga

cek = uang_kamu > total_harga

rincian_biaya = f"""
\n Harga buku       : {total_harga}
\n Kembalian uang   : {kembalian}
\n Cek              : {cek}

"""

print (rincian_biaya)