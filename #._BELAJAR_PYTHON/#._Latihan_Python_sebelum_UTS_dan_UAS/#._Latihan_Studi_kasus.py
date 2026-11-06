print ("Hello World")

print ("\n --- batas --- \n")


# Studi kasus pemilihan buku 

pilih_buku = input ("Masukkan buku apa kamu mau pilih = ")

if pilih_buku == "komik":
    harga = 5000
    print ("Pilihan kamu komik")

elif pilih_buku == "novel":
    harga = 4000
    print ("Pilihan kamu novel")

elif pilih_buku == "buku mapel":
    harga = 6000
    print ("Pilihan kamu buku mapel")

elif pilih_buku == "buku masak":
    harga = 6000
    print ("Pilihan kamu buku masak")

elif pilih_buku == "buku panduan elektronik":
    harga = 7000
    print ("Pilihan kamu buku panduan elektronik")

elif pilih_buku == "buku coding":
    harga = 8000
    print ("Pilihan kamu buku coding")

else:
    print ("Input tidak valid")


print = f"Buku pilihan kamu = {pilih_buku} dan dengan harga = {harga}"

print ("\n --- batas --- \n")