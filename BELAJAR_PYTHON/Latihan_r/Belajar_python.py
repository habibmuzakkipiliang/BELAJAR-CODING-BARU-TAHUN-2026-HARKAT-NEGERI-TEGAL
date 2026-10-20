print ("Hello World")


print ("\n --- batas --- \n")




# variabel dasar

a = 19
print (a)

b = "Halo Dunia"
print (b)

c = 12
print (c)

d = True
print (d)


print ("\n --- batas --- \n")





# Fungsi dengan operator 

x = int (input ("Masukkan angka x = "))
y = int (input ("Masukkan angka y = "))

def tambah (x, y):
     return x + y

def kurang (x, y):
     return x - y

def kali (x, y):
     return x * y

def bagi (x, y):
     return x / y

def mod (x, y):
     return x % y

print ("Tambah =", tambah (x, y))
print ("Kurang =", kurang (x, y))
print ("Kali =", kali (x, y))
print ("Bagagi =", bagi (x, y))
print ("Mod =", mod (x, y))


print ("\n --- batas --- \n")



# percabangan dasar

a = 9

if a >= 8:
     print (f"besar, angka a = {a}")

else:
     print (f"kecil, angka a = {a}")


print ("\n --- batas --- \n")




# percabangan lanjutan

b = 3

if b >= 8:
     print (f"besar, angka b = {b}")

elif b >= 5:
     print (f"sedang, angka b = {b}")

else:
     print (f"kecil, angka b = {b}")


print ("\n --- batas --- \n")




# Fungsi dengan percabangan dasar

def run (a):

     if a >= 5:
          print (f"besar, angka a = {a}")

     else:
          print (f"kecil, angka a = {a}")

run (10)
run (9)
run (8)
run (7)
run (6)
run (5)
run (4)
run (3)
run (2)
run (1)



print ("\n --- batas --- \n")




hal = [
     "Linux Mint",
     "Linux Ubuntu",
     "Linux Debian",
     "Linux Kubuntu",
     "Linux Asli"
]

for b in hal:
     print (b)


print ('\n -- batas --- \n')




# Array 

fer = [
     "Gracie JKT48",
     "Aralie JKT48",
     "Fritzy JKT48",
     "Halo Dunia"
]

fer.append ("Hayyan")
fer.append ("Rayyan")
fer.append ("Koper")

for r in fer:
     print (r)


print ("\n --- batas --- \n")