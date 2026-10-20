tem = """
========================================================

\t\t TOKO SEMBAKO NIKSON DAN BANG ARIL 

========================================================

"""

print (tem)


roti = 3000
air_minum_500ml = 5000
air_minum_1500ml = 6000
makanan_ringan = 7000
air_teh_manis_dingin = 7000
nasi = 6000
deterjen = 8000
sabun_mandi = 8000
kelontong = 8000
mie_lidi = 3000
sate_taichan = 6000
sate_daging_kambing = 8000
nasi_goreng = 9000
nasi_kuning = 7000
nasi_ayam_geprek = 8000
pembersih_lantai = 5000
pembersih_toilet = 5000


nama_pesan1 = str (input ("Masukkan nama pesan 1 = "))
nama_pesan2 = str (input ("Masukkan nama pesan 2 = "))
nama_pesan3 = str (input ("Masukkan nama pesan 3 = "))
nama_pesan4 = str (input ("Masukkan nama pesan 4 = "))
nama_pesan5 = str (input ("Masukkan nama pesan 5 = "))
nama_pesan6 = str (input ("Masukkan nama pesan 6 = "))
nama_pesan7 = str (input ("Masukkan nama pesan 7 = "))


jumlah_ayam_geprek = int (input ("berapa ayam geprek nya = "))
jumlah_nasi_goreng = int (input ("berapa nasi goreng nya = "))
jumlah_nasi_kuning = int (input ("berapa nasi kuning nya = "))
jumlah_sate_taichan = int (input ("berapa sate taichan nya = "))
jumlah_mie_lidi = int (input ("berapa mie lidi nya = "))
jumlah_sabun_mandi = int (input ("berapa sabung mandi =  "))
jumlah_roti = int (input ("berapa roti nya = "))
jumlah_kelontong = int (input ("berapa kelontong nya = "))
jumlah_sate_daging = int (input ("berapa sate daging nya = "))
jumlah_deterjen = int (input ("berapa deterjen nya = "))
jumlah_air_teh_manis_dingin = int (input ("berapa air teh manis dingin nya = "))
jumlah_nasi = int (input ("berapa nasi nya = "))
jumlah_air_minum_500ml = int (input ("berapa air minum 500 ml nya = "))
jumlah_air_minum_1500ml = int (input ("berapa air minum 1500 ml nya = "))
jumlah_pembersih_toilet = int (input ("berapa pembersih toilet nya = "))
jumlah_pembersih_lantai = int (input ("berapa pembersih lantai nya = "))


a1 = jumlah_air_teh_manis_dingin * air_teh_manis_dingin
a2 = jumlah_air_minum_500ml * air_minum_500ml
a3 = jumlah_air_minum_1500ml * air_minum_1500ml
a4 = jumlah_ayam_geprek * nasi_ayam_geprek
a5 = jumlah_sate_taichan * sate_taichan
a6 = jumlah_deterjen * deterjen
a7 = jumlah_mie_lidi * mie_lidi
a8 = jumlah_nasi * nasi
a9 = jumlah_nasi_kuning * nasi_kuning
a10 = jumlah_nasi_goreng * nasi_goreng
a11 = jumlah_kelontong * kelontong
a12 = jumlah_sabun_mandi * sabun_mandi
a13 = jumlah_sate_daging * sate_daging_kambing
a14 = jumlah_pembersih_lantai * pembersih_lantai 
a15 = jumlah_pembersih_toilet * pembersih_toilet

uang_kamu = int (input ("Uang kamu ada berapa = "))

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15

kembalian = uang_kamu - total

cek = uang_kamu > total

rincian = f"""
========================================

\t RINCIAN PEMESANAN KAMU 

========================================

- Nama pemesan 1        : {nama_pesan1}
- Nama pemesan 2        : {nama_pesan2}
- Nama pemesan 3        : {nama_pesan3}
- Nama pemesan 4        : {nama_pesan4}
- Nama pemesan 5        : {nama_pesan5}
- Nama pemesan 6        : {nama_pesan6}
- Nama pemesan 7        : {nama_pesan7}
- Total pembayaran      : {total}
- Kembalian             : {kembalian}
- Cek                   : {cek}

Terimakasih telah membeli di Toko Sembako Kami

"""

print (rincian)




