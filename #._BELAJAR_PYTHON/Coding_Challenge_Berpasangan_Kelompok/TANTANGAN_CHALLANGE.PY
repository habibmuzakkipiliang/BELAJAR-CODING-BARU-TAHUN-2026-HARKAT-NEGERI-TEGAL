nama_anggota_1 = "Habib Muzakki"
nama_anggota_2 = "Destario Dwi Abdillah"
nim_anggota_1 = 26090040
nim_anggota_2 = 26090026
kelas = "1B"
jurusan = "D4 Teknik Informatika"
fakultas = "Sekolah Vokasi"
kampus = "Universitas Harkat Negeri"
kota = "Kota Tegal, Jawa Tengah"


print("===Rincian Pemesana Tiket Bioskop===")
print("Daftar Nama Bioskop\n1. CGV.\n2. CINEPOLIS\n3. GAJAH MADA")

Bioskop = str(input("Nama Bioskop: "))
print("\nPilih Genre:\n1. Horor\n2. Romance\n3. Komedi")
Genre= str(input("Pilih Genre: "))
HargaTiket = 50000
tiket = int(input ("\nMau Tiket Berapa?: "))
Total_Harga_Tiket = tiket * HargaTiket 

nama1 = str(input("Nama Pemesan 1: "))
nama2 = str(input("Nama Pemesan 2: "))

print("\nDaftar Harga Makanan/Minuman:\n1. Popcorn \t: Rp. 30.000\n2. Aqua \t: Rp. 5.000")
Popcorn = 30000
Aqua = 5000

Pop = int(input("Mau Pesen Popcorn Berapa?: "))
Aqu = int(input("Mau Pesen Aqua Berapa?: ")) 
Totalpopcorn= Popcorn * Pop
Totalaqua =  Aqua * Aqu
Uang = int(input("Masukkan uang yang dibayarkan: "))


Total_keseluruhan = Total_Harga_Tiket + Totalpopcorn + Totalaqua
Lebih = Uang > Total_keseluruhan

Kembalian = Uang - Total_keseluruhan


print ("\n=== TANTANGAN CODING BERPASANGAN KELOMPOK ===")
print(f"Nama Anggota 1 \t: {nama_anggota_1}({nim_anggota_1})")
print(f"Nama Anggota 2 \t: {nama_anggota_2}({nim_anggota_2})")
print(f"Kelas \t\t: {kelas}")
print(f"Jurusan \t: {jurusan}")
print(f"Fakultas \t: {fakultas}")
print(f"Kampus \t\t: {kampus}")
print(f"Kota \t\t: {kota}")

print("\n\n========================================")
print("\tRINCIAN PEMESANAN BIOSKOP")
print("========================================\n")


print(f"Nama Bioskop \t\t: {Bioskop}")
print(f"Genre Film \t\t: {Genre}")
print(f"Jumlah tiket \t\t: {tiket} Tiket")
print(f"Total Harga Tiket \t: Rp. {Total_Harga_Tiket}")
print(f"Nama Pemesan 1 \t\t: {nama1}")
print(f"Nama Pemesan 2 \t\t: {nama2}")
print(f"Jumlah Popcorn \t\t: {Pop} Popcorn")
print(f"Jumlah Aqua \t\t: {Aqu} Aqua")
print(f"Total Keseluruhan \t: Rp. {Total_keseluruhan}")
print(f"Uang yang dibayarkan \t: Rp. {Uang}")
print(f"Apakah Ada Uang Sisa? \t: {Lebih}")
print(f"Kembalian \t\t: Rp. {Kembalian}")

print(f"\nTerima Kasih {nama1} dan {nama2} Telah Memesan Tiket Bioskop di {Bioskop}\nDengan Genre Film {Genre}\nSemoga Memuaskan dan Selamat Menonton :) ")