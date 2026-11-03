print ("Selamat datang di Toko Buku Nikson")

nama = "Habib Muzakki"
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Vokasi"
coding = "HTML, CSS, JavaScript dan Python"
tools = "Github, Github Pages, Vercel, Netlify"

bio = f"""
- Nama lengkap  : {nama}
- Kelas         : {kelas}
- Jurusan       : {jurusan}
- Fakultas      : {fakultas}
- Coding        : {coding}
- Tools         : {tools}
"""

print (bio)

print ("\n --- batas --- \n")




buku_novel = 7000
buku_cerita_rakyat = 8000
buku_tulis = 4000
buku_komik = 6000
majalah = 5000
ensiklopedia = 10000

jumlah_buku_cerita_rakyat = int (input ("Masukkan buku cerita = "))
jumlah_buku_tulis = int (input ("Masukkan buku tulis = "))
jumlah_majalah = int (input ("Masukkan majalah = "))
jumlah_ensiklopedia = int (input ("Masukkan ensiklopedia = "))

b1 = jumlah_buku_cerita_rakyat * buku_cerita_rakyat
b2 = jumlah_buku_tulis * buku_tulis
b3 = jumlah_ensiklopedia * ensiklopedia
b4 = jumlah_majalah * majalah

total = b1 + b2 + b3 + b4

uang_kamu = int (input ("Masukkan uang kamu = "))

kembalian = total - uang_kamu

cek = total > uang_kamu

bayar = f"""
- Total        : {total}
- Kembalian    : {kembalian}
- Cek          : {cek}

"""

print (bayar)