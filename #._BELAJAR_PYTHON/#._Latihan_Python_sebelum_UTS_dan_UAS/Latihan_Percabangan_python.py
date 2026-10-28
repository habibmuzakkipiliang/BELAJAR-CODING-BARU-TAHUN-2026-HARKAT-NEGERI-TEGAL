print ("""
=====================================================================================

USIA MASUK DAN JOIN JKT48 TAHUN 2026 

======================================================================================

""")

status = str (input ("Masukkan jenjang pendidikan atau kerja atau nikah kamu  = "))
usia = int (input ("Masukkan usia kamu sekarang ini (15 - 19) = "))

if status == "Kerja":
    if usia >= 13 and usia <= 19:
        print (f"Usia dan status sudah mencukupi persyaratan, usia = {usia} dan status = {status}")

    else:
        print (f"kamu sudah mencukupi usia, tapi belum mencukupi kerja, usia = {usia} dan status = {status}")


elif status == "Mahasiswa":
    if usia >= 13 and usia <= 18:
        print (f"Usia sudah mencukupi dan sudah mencukupi status nya, usia = {usia} dan status = {status}")

    else:
        print (f"Belum mencukupi usia dan status nya, usia = {usia} dan status = {status}")

elif status == "SMA atau MAN":
    if usia >= 13 and usia <= 19:
        print (f"usia kamu sudah tercapai dan status sudah oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi, usia = {usia} dan status = {status}")


elif status == "SMP":
    if usia >= 13 and usia <= 19:
        print (f"usia sudah mencukupi dan status nya juga oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi saat ini, usia = {usia} dan status = {status}")

elif status == "SD":
    if usia >= 13 and usia <= 18:
        print (f"Usia sudah mencukupi dan status juga oke, usia = {usia} dan status = {status}")

    else:
        print (f"Usia dan status belum mencukupi, usia = {usia} dan status = {status}")

else:
    print ("Input invalid")


print ("\n --- batas --- \n")