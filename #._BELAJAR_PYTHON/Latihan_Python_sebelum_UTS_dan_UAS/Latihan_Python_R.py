# Switch lampus lalu lintas 

lampu = int (input ("Masukkan lampu lalu lintas saat ini : "))

match (lampu):

    case "Merah":
        print ("Warna merah, berhenti")

    case "Kuning":
        print ("Warna kuning, bersiap-siap")

    case "Hijau":
        print ("Warna hijau, jalan")

    case _:
        print ("Input tidak valid")


print ("\n --- batas --- \n")




