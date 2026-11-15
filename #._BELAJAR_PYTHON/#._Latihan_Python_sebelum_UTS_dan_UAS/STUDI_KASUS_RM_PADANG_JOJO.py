print ("""
=====================================================================================

STUDI KASUS TENTANG SISTEM PEMBAYARAN RUMAH MAKAN PADANG MILIK UDA JOJO (Junior Muhammad Hendri)

=====================================================================================
""")

# Alamat lengkap rumah makan padang Uda Jojo (Junior Muhammad Hendri)

nama = "Rumah Makan Padang Uda Jojo"
asal_daerah = "Kota Padang, Sumbar"
alamat = "Jl Martapura, Margadana, Pasurungan Lor, Kota Tegal"
pemilik = "Uda Jo"
nama_asli_pemilik = "Junior Muhammad Hendri"
dibangun = "tahun 2026"
jurusan = "S1 Teknik Mesin"
fakultas = "Sains dan Teknologi"
kampus = "Universitas Harkat Negeri Tegal"

detail = f"""
- Nama toko     : {nama}
- Asal daerah   : {asal_daerah}
- Alamat        : {alamat}
- Pemilik       : {pemilik}
- Nama asli     : {nama_asli_pemilik}
- Dibangun      : {dibangun}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Kampus        : {kampus} 


"""

print (detail)


nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))
nama_pemesan4 = str (input ("Masukkan nama pemesan 4 = "))


biaya_parkir = 1000
nasi = 3000
ayam_rendang = 4000
ayam_gulai_rendang = 5000
daging_sapi_rendang = 6000
daging_ayam_rendang = 3000
sayur_singkong = 6000
sayur_bayam = 3000
sayur_kuah_nangka = 4000
teh_manis_anget = 0
teh_manis_es = 0
aqua = 0


j_biaya_parkir = int (input ("Berapa biaya parkir nya = "))
j_nasi = int (input ("Berapa jumlah porsi nasi nya = "))
j_ayam_rendang = int (input ("Berapa ayam rendang nya = "))
j_ayam_gulai_rendang = int (input ("Berapa ayam gulai rendang nya = "))
j_daging_sapi_rendang = int (input ("Berapa daging sapi rendang nya = "))
j_daging_ayam_rendang = int (input ("Berapa daging ayam rendang nya = "))
j_sayur_singkong = int (input ("Berapa sayur singkong nya = "))
j_sayur_bayam = int (input ("Berapa sayur bayam nya = "))
j_sayur_kuah_nangka = int (input ("Berapa sayur kuah nangka nya = "))
j_teh_manis_anget = int (input ("Berapa teh manis anget nya = "))
j_teh_manis_es = int (input ("Berapa teh manis es nya = "))
j_aqua = int (input ("Berapa aqua nya = "))


a1 = j_aqua * aqua
a2 = j_ayam_gulai_rendang * ayam_gulai_rendang
a3 = j_daging_ayam_rendang * daging_ayam_rendang
a4 = j_daging_sapi_rendang * daging_sapi_rendang
a5 = j_nasi * nasi
a6 = j_biaya_parkir * biaya_parkir
a7 = j_ayam_rendang * ayam_rendang 
a8 = j_sayur_bayam * sayur_bayam
a9 = j_sayur_kuah_nangka * sayur_kuah_nangka
a10 = j_teh_manis_es * teh_manis_es 
a11 = j_teh_manis_anget * teh_manis_anget

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian_biaya = f"""
======================================================================================

RINCIAN PEMBAYARAN RUMAH MAKAN PADANG MILIK UDA JOJO (Junior Muhammad Hendri)

======================================================================================

- Nama pemesan 1    : {nama_pemesan1}
- Nama pemesan 2    : {nama_pemesan2}
- Nama pemesan 3    : {nama_pemesan3}
- Nama pemesan 4    : {nama_pemesan4}
- Uang kamu         : {uang_kamu}
- Total biaya       : {total}
- Cek               : {cek}

"""

print (rincian_biaya)


print ("\n --- batas --- \n")




print ("""
======================================================================================

RATING PENILAIAN RUMAH MAKAN PADANG UDA JOJO (JUNIOR MUHAMMAD HENDRI)

======================================================================================
""")

rating = int (input ("Masukkan rating nya (1 - 10) = "))

if rating >= 10:
    print (f"A+, rating = {rating}")

elif rating >= 9:
    print (f"A-, rating = {rating}")

elif rating >= 8:
    print (f"B+, rating = {rating}")

elif rating >= 7:
    print (f"B-, rating = {rating}")

elif rating >= 6:
    print (f"C, rating = {rating}")

elif rating >= 5:
    print (f"D, rating = {rating}")

elif rating >= 4:
    print (f"E, rating = {rating}")

elif rating >= 3:
    print (f"F, rating = {rating}")

elif rating >= 2:
    print (f"Jelek -, rating = {rating}")

elif rating >= 1:
    print (f"Jelek --, rating = {rating}")

else:
    print (f"Input tidak valid, rating = {rating}")



print ("\n --- batas --- \n")





print ("""
=====================================================================================

SISTEM PRAKIRAAN CUACA DENGAN SEDERHANA DAN MUDAH AJA

======================================================================================

""")

cuaca = str (input ("Masukkan cuaca hari ini = (cerah, berawan, angin, hujan)"))
suhu = int (input ("Masukkan suhu berapa derajat = (dalam Celcius) : "))

if cuaca == "Cerah":
    if suhu > 25:
        print ("Sudah cerah dan boleh keluar rumah")

    else:
        print ("Gak boleh keluar rumah, karena panas banget")

elif cuaca == "Berawan":
    if suhu < 30:
        print ("Adem udaranya, dan boleh keluar rumah")

    else:
        print ("Gak boleh keluar rumah")

elif cuaca == "Hujan":
    if suhu < 30:
        print ("Gak boleh keluar rumah")

    else:
        print ("Boleh bawa payung")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")



print ("""
=====================================================================================

USIA MASUK DAN JOIN JKT48

======================================================================================

""")

usia_jkt48 = int (input ("Masukkan usia kamu sekarang = "))

if usia_jkt48 >= 13 and usia_jkt48 <= 18:
    print (f"Usia kamu sudah untuk join JKT48, usia = {usia_jkt48}")

elif usia_jkt48 >= 18:
    print (f"Usia kamu sudah lebih dari cukup, usia = {usia_jkt48}")

else:
    print (f"Usia kamu masih kecil, usia = {usia_jkt48}")


print ("\n --- batas --- \n")