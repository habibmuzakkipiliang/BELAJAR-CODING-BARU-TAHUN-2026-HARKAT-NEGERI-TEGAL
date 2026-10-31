print ("Selamat datang di CFD Rest Area Tol Semarang - Batang")

ayam = 30000
nasi = 20000
minum = 2000
es_teh = 6000
teh_anget = 4000


jumlah_ayam = int (input ("Masukkan jumlah ayam = "))
jumlah_nasi = int (input ("Masukkan porsi nasi = "))
minum = int (input ("Masukkan minum berapa = "))
jumlah_es_teh = int (input ("Masukkan es teh ="))
jumlah_teh_anget = int (input ("Masukkan teh anget ="))


uang_kamu = int (input ("Masukkan uang kamu ="))

t_1 = jumlah_ayam * ayam
t_2 = jumlah_nasi * nasi
t_3 = jumlah_teh_anget * teh_anget
t_4 = jumlah_es_teh * es_teh

jumlah = t_1 + t_2 + t_3 + t_4

cek = uang_kamu < jumlah

kembalian = uang_kamu - jumlah

rio = f"""
- Total pembayaran  : {jumlah}
- Kembalian         : {kembalian}
- Cek               : {cek}
"""

print (rio)