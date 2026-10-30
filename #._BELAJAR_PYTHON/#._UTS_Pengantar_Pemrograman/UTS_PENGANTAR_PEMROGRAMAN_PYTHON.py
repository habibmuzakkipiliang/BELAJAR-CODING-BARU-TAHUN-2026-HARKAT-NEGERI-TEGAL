print ("""
======================================================================================

\t\t UTS (Ujian Tengah Semester) PENGANTAR PEMRORGAMAN TAHUN 2026 

======================================================================================

""")



# Tes Hello World Python dulu (tujuan nya untuk mengetes Program jalan atau tidak)

print ("Halo Selamat Pagi")


print ("\n --- batas --- \n")




# Variabel awalan dulu (Tujuan nya supaya bisa jalankan variabelnya atau tidak)

print ("""
=====================================================================================

\t\t\t Variabel awalan 

=====================================================================================

""")

kuliah = "- Selamat pagi Universitas Harkat Negeri Tegal"
print (kuliah)

jurusan = "- D4 Teknik Informatika"
print (jurusan)

jkt48 = "- Selamat Fx Sudirman JKT48, Jakarta Pusat"
print (jkt48)

oshi = """
- Selamat pagi Gracie JKT48
- Selamat pagi Aralie JKT48
- Selamat pagi Lily JKT48
- Selamat pagi Jemima JKT48
"""

print (oshi)

print ("\n --- batas --- \n")



# Biodata lengkap Habib Muzakki (dengan tujuan untuk memperjelas data lengkap saya sebelum dinilai)

nama_lengkap = "Habib Muzakki"
nama_panggilan = "Habib"
asal_daerah = "Kota Serang, Banten"
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
nim = 26090040
golongan_darah = "B"
kampus = "1 Mataram (Universitas Harkat Negeri)"
hobi = "Ngewota oshi JKT48, denger musik JKT48, denger musik Phonk (untuk Coding)"
oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Jemima JKT48"]


bio = f"""
=====================================================================================

\t\t\t BIODATA LENGKAP HABIB MUZAKKI 

======================================================================================

\n - Nama lengkap       : {nama_lengkap}
\n - Nama panggilan     : {nama_panggilan}
\n - Asal daerah        : {asal_daerah}
\n - Kelas              : {kelas}
\n - Jurusan            : {jurusan}
\n - Fakultas           : {fakultas}
\n - NIM                : {nim}
\n - Golongan darah     : {golongan_darah}
\n - Kampus Universitas : {kampus}
\n - Hobi               : {hobi}

"""

print (bio)

for j in oshi:
    print ("Oshi JKT48 =", j)

print ("\n --- batas --- \n")



# Studi kasus tentang sistem pembayaran detail Warung Nasi milik Nikson dan Gon NTT (Tujuan untuk Materi Variabel, input, output, dan operator aritmatika)

print ("""
======================================================================================

Studi kasus tentang sistem pembayaran detail Warung Nasi milik Nikson dan Gon NTT

======================================================================================
""")

nama_pemesan1 = str (input ("Masukkan nama pemesan 1 = "))
nama_pemesan2 = str (input ("Masukkan nama pemesan 2 = "))
nama_pemesan3 = str (input ("Masukkan nama pemesan 3 = "))

nasi_campur = 5000
nasi_lengko = 6000
nasi_ayam_geprek = 7000
nasi_ayam_ijo = 8000
nasi_ayam_goreng = 9000
nasi_goreng = 10000
nasi_ayam_bakar = 8000
nasi_ayam_lado = 9000


j_nasi_ayam_goreng = int (input ("Masukkan jumlah porsi nasi ayam goreng nya = "))
j_nasi_goreng = int (input ("Masukkan jumlah porsi nasi goreng = "))
j_nasi_ayam_bakar = int (input ("Masukkan jumlah porsi nasi ayam goreng = "))
j_nasi_ayam_lado = int (input ("Masukkan jumlah porsi nasi ayam lado = "))
j_nasi_campur = int (input ("Masukkan jumlah porsi nasi campur = "))
j_nasi_lengko = int (input ("Masukkan jumlah porsi nasi lengko = "))
j_nasi_ayam_geprek = int (input ("Masukkan jumlah porsi nasi ayam geprek = "))
j_nasi_ayam_ijo = int (input ("Masukkan jumlah porsi nasi ayam ijo = "))

a1 = j_nasi_ayam_bakar * nasi_ayam_bakar
a2 = j_nasi_ayam_geprek * nasi_ayam_geprek
a3 = j_nasi_ayam_goreng * nasi_ayam_goreng
a4 = j_nasi_ayam_ijo * nasi_ayam_ijo
a5 = j_nasi_campur * nasi_campur
a6 = j_nasi_lengko * nasi_lengko
a7 = j_nasi_ayam_lado * nasi_ayam_lado
a8 = j_nasi_goreng * nasi_goreng

total_semua = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total_semua

cek = kembalian > total_semua


rincian_biaya = f"""
=====================================================================================

RINCIAN PEMBAYARAN DETAIL WARUNG NASI MILIK NIKSON DAN GON NTT

=====================================================================================


\n - Nama pemesan 1        : {nama_pemesan1}
\n - Nama pemesan 2        : {nama_pemesan2}
\n - Nama pemesan 3        : {nama_pemesan3}
\n - Total semua           : {total_semua}
\n - Uang kamu             : {uang_kamu}
\n - Cek                   : {cek}

"""

print (rincian_biaya)


print ("\n --- batas --- \n")




# Percabangan UTS Tentang Nilai Akhir UTS (Tujuan untuk menentukan Grade nya sesuai nilai yang pas)

print ("""
======================================================================================

Percabangan UTS Tentang Nilai Akhir UTS

======================================================================================
""")

nilai = int (input ("Masukkan nilai kamu = "))

if nilai >= 95:
    print (f"nilai A+, nilai = {nilai}")

elif nilai >= 90:
    print (f"Nilai A-, nilai = {nilai}")

elif nilai >= 85:
    print (f"Nilai B+, nilai = {nilai}")

elif nilai >= 80:
    print (f"Nilai C, nilai = {nilai}")

elif nilai >= 75:
    print (f"Nilai D, nilai = {nilai}")

elif nilai >= 70:
    print (f"Nilai E, nilai = {nilai}")

elif nilai >= 60:
    print (f"Nilai F, nilai = {nilai}")

else:
    print (f"Input tidak valid")


print ("\n --- batas --- \n")


print ("""
======================================================================================

Terimakasih sudah mencoba menjalankan Program ini.

Salam dari Habib Muzakki

Salam dari Kota Serang, Banten

======================================================================================
""")