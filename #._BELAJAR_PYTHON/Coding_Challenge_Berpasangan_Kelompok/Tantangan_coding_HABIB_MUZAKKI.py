print (" \n ============= TANTANGAN CODING BERPASANGAN KELOMPOK ============")

nama_anggota_1 = "Habib Muzakki"
nama_anggota_2 = "Destario Dwi Abdillah"
nim_anggota_1 = 26090040
nim_anggota_2 = 26090026
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
kampus = "Universitas Harkat Negeri (Eks Politeknik Harapan Bersama)"
kota = "Kota Tegal, Jawa Tengah"

data_kelompok = f"""
\n - Nama anggota 1    :  {nama_anggota_1}
\n - Nama anggota 2    :  {nama_anggota_2}
\n - NIM anggota 1     :  {nim_anggota_1}
\n - NIM anggota 2     :  {nim_anggota_2}
\n - Kelas             :  {kelas}
\n - Jurusan           :  {jurusan}
\n - Fakultas          :  {fakultas}
\n - Kota              :  {kota}

"""

print (data_kelompok)

print ("\n ---- batas --- \n")



bioskop_tempat = """

========================= RINCIAN DAFTAR BIOSKOP =============================

\n 1. Cgv
\n 2. Cinepolis
\n 3. Gajah Mada

"""

print (bioskop_tempat)



nama_bioskop = str (input ("Pilih nama bioskop = "))

genre_film = """

======================= GENRE FILM ==========================

\n 1. Horor
\n 2. Romance
\n 3. Komedi

"""

print (genre_film)



genre = str (input ("Pilih Genre Film nya = "))

harga_tiket = 55000

jumlah_tiket = int (input ("Mau tiket berapa = "))

total_tiket = jumlah_tiket * harga_tiket



nama_1 = str (input ("Nama pemesan 1 = "))
nama_2 = str (input ("Nama pemesan 2 = "))


daftar_menu = """

=================== DAFTAR MENU MAKANAN DAN MINUMAN ===================

\n 1. Popcorn = 30000
\n 2. Aqua    = 5000

"""

print (daftar_menu)



harga_popcorn = 30000
harga_aqua = 5000


jumlah_popcorn = int (input ("Mau pesen popcorn berapa = "))
jumlah_aqua = int (input ("Mau pesen aqua berapa = "))


total_popcorn = jumlah_popcorn * harga_popcorn
total_aqua = jumlah_aqua * harga_aqua


uang_kamu = int (input ("Masukkan uang yang dibayarkan = "))

total_keseluruhan = total_tiket + total_aqua + total_popcorn

cek_data = uang_kamu > total_keseluruhan

kembalian_uang = uang_kamu - total_keseluruhan



rincian_semua_informasi = f"""

================== RINCIAN SEMUA INFORMASI KAMU ======================

\n - Nama Tempat bioskop  :  {nama_bioskop}
\n - Genre film           :  {genre}
\n - Jumlah tiket         :  {jumlah_tiket}
\n - Total tiket          :  {total_tiket}
\n - Nama pemesan 1       :  {nama_1}
\n - Nama pemesan 2       :  {nama_2}
\n - Jumlah popcorn       :  {jumlah_popcorn}
\n - Jumlah Aqua          :  {jumlah_aqua}
\n - Total popcorn        :  {total_popcorn}
\n - Total Aqua           :  {total_aqua}
\n - Uang kamu            :  {uang_kamu}
\n - Total keseluruhan    :  {total_keseluruhan}
\n - Cek data fakta       :  {cek_data}
\n - Kembalian uang       :  {kembalian_uang}
"""

print (rincian_semua_informasi)



