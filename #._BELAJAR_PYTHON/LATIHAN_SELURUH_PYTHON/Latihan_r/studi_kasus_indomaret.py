# Hello World

print ("Hello World")

print ("Pemilik oleh Habib Muzakki D4 Teknik Informatika")

infor = "Semangat untuk coding nya"
print (infor)


print ("\n --- batas --- \n")



# studi kasus indomaret 

roti = 6000
minum_500ml = 3000
minum_15000ml = 5000
chiki = 7000
mie_instan = 8000
pop_mie = 8000
coca_cola = 8000
ayam_geprek = 6000
ayam_goreng = 8000
nasi_goreng = 10000
nasi = 4000
susu_uht_500ml = 3000
susu_uht_1500ml = 8000
roti_kasur = 10000
air_teh_manis = 5000


jumlah_pop_mie = int (input ("Masukkan jumlah pop mie = "))
jumlah_mie_instan = int (input ("Masukkan jumlah mie instan = "))
jumlah_nasi = int (input ("Masukkan jumlah nasi = "))
jumlah_chiki = int (input ("Masukkan jumlah chiki = "))
jumlah_minum_500ml = int (input ("Masukkan jumlah minum 500 ml = "))
jumlah_minum_1500ml = int (input ("Masukkan jumlah minum 1500 ml = "))
jumlah_coca_cola = int (input ("Masukkan jumlah coca cola = "))
jumlah_nasi_goreng = int (input ("Masukkan jumlah nasi goreng = "))
jumlah_ayam_goreng = int (input ("Masukkan jumlah ayam goreng = "))
jumlah_ayam_geprek = int (input ("Masukkan jumlah ayam geprek = "))
jumlah_susu_uht_500ml = int (input ("Masukkan jumlah susu uht 500 ml = "))
jumlah_susu_uht_1500ml = int (input ("Masukkan jumlah sus uht 1500 ml = "))
jumlah_roti_kasur = int (input ("Masukkan jumlah roti kasur = "))
jumlah_air_teh_manis = int (input ("Masukkan jumlah air teh manis = "))

uang_kamu = int (input ("Masukkan uang kamu = "))

a1 = jumlah_chiki * chiki
a2 = jumlah_mie_instan * mie_instan
a3 = jumlah_minum_1500ml * minum_15000ml
a4 = jumlah_minum_500ml * minum_500ml
a5 = jumlah_coca_cola * coca_cola
a6 = jumlah_pop_mie * pop_mie
a7 = jumlah_ayam_geprek * ayam_geprek 
a8 = jumlah_ayam_goreng * ayam_goreng
a9 = jumlah_nasi_goreng * nasi_goreng
a10 = jumlah_roti_kasur * roti_kasur
a11 = jumlah_air_teh_manis * air_teh_manis

total = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11

kembalian = total - uang_kamu

cek = total > uang_kamu

info = f"""
- Total bayar semua     : {total}
- Kembalian             : {kembalian}
- Cek                   : {cek}
"""

print (info)


print ("\n --- batas --- \n")





