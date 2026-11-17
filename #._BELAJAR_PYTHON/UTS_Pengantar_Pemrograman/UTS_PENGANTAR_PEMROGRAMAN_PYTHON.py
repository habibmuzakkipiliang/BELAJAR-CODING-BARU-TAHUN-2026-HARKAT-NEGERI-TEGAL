print ("""
======================================================================================

\t\t UTS (Ujian Tengah Semester) PENGANTAR PEMRORGAMAN TAHUN 2026 

======================================================================================

""")



# Tes Hello World Python dulu (tujuan nya untuk mengetes Program jalan atau tidak)

print ("Hello World")


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
github = "https://github.com/habibmuzakkipiliang (habibmuzakkipiliang)"
linkedin = "https://www.linkedin.com/in/habib-muzakki-piliang-15978b315/ (linkedin)"
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
nim = 26090040
golongan_darah = "B"
kampus = "1 Mataram (Universitas Harkat Negeri)"
hobi = "Ngewota oshi JKT48, denger musik JKT48, denger musik Phonk (untuk Coding)"
oshi = ["Gracie JKT48", "Aralie JKT48", "Lily JKT48", "Jemima JKT48", "Fritzy JKT48"]


bio = f"""
=====================================================================================

\t\t\t BIODATA LENGKAP HABIB MUZAKKI 

======================================================================================

\n - Nama lengkap       : {nama_lengkap}
\n - Nama panggilan     : {nama_panggilan}
\n - Asal daerah        : {asal_daerah}
\n - Github             : {github}
\n - Linkedin           : {linkedin}
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



print ("""
======================================================================================

Studi kasus tentang program kasir sederhana

======================================================================================
""")

daftar_barang = ("""
\n topi = 20000
\n jaket = 30000
\n kaos = 50000
\n kacamata gaya = 20000
\n jam tangan = 90000
""")

print (daftar_barang)


nama_barang1 = str (input ("Masukkan nama barang 1 = "))
nama_barang2 = str (input ("Masukkan nama barang 2 = "))
nama_barang3 = str (input ("Masukkan nama barang 3 = "))


topi = 20000
jaket = 30000
kaos = 50000
kacamata_gaya = 20000
jam_tangan = 90000


j_topi = int (input ("Masukkan jumlah topi = "))
j_jaket = int (input ("Masukkam jumlah jaket = "))
j_kaos = int (input ("Masukkan jumlah kaos = "))
j_kacamata_gaya = int (input ("Masukkan jumlah kacamata gaya = "))
j_jam_tangan = int (input ("Masukkan jumlah jam tangan = "))


a1 = j_topi * topi
a2 = j_jaket * jaket
a3 = j_kaos * kaos
a4 = j_kacamata_gaya * kacamata_gaya
a5 = j_jam_tangan * jam_tangan



total_semua = a1 + a2 + a3 + a4 + a5

if total_semua >= 100000:
    print (total_semua * 0.10)

else:
    print (0)


uang_kamu = int (input ("Masukkan uang kamu sekarang = "))

kembalian = uang_kamu - total_semua

cek = uang_kamu > total_semua


rincian_biaya = f"""
=====================================================================================

RINCIAN PEMBAYARAN SISTEM PEMBAYARAN KASIR SEDERHANA

=====================================================================================

\n - Nama barang 1            : {nama_barang1}
\n - Nama barang 2            : {nama_barang2}
\n - Nama barang 3            : {nama_barang3}
\n - Total semua                 : {total_semua}
\n - Uang kamu                   : {uang_kamu}
\n - Cek                                : {cek}

"""

print (rincian_biaya)


print ("\n --- batas --- \n")




print ("""
======================================================================================

\t Percabangan UTS, UAS, TUGAS, NILAI AKHIR (Tujuan untuk menentukan Grade nya sesuai nilai yang pas)

======================================================================================
""")

nama_kamu = str (input ("Masukkan nama kamu sekarang = "))
uts = int (input ("Masukkan nilai UTS kamu = "))
uas = int (input ("Masukkan nilai UAS kamu = "))
tugas = int (input ("Masukkan nilai tugas kamu = "))

nilai_akhir = (tugas * 0.3) + (uts  * 0.3) + (uas * 0.4)

nilai_akhir = uts + uas + tugas

if nilai_akhir < 0 or nilai_akhir > 100:
    if nilai_akhir >= 85:
        print ("Grade = A")

    elif nilai_akhir >= 75:
        print ("Grade = B")

    elif nilai_akhir >= 65:
        print ("Grade = C")

    elif nilai_akhir >= 50:
        print ("Grade = D")

    else:
        print ("Grade = E")

else:
    print ("Input tidak valid")


print ("\n --- batas --- \n")


print (f"""

===============================================================================


\t\t\t RINCIAN NAMA DAN NILAI KAMU (KETERANGAN YANG LENGKAP DAN JELAS)

===============================================================================

\n Nama kamu        : {nama_kamu}
\n Nilai UTS        : {uts}
\n Nilai UAS             : {uas}
\n Nilai Tugas          : {tugas}
\n Nilai akhir           : {nilai_akhir}

""")


print ("\n --- batas --- \n")


print ("""
======================================================================================

Terimakasih sudah mencoba menjalankan Program ini.

Salam dari Habib Muzakki

Salam dari Kota Serang, Banten

Salam dari Wota JKT48 asal Kota Serang

======================================================================================
""")