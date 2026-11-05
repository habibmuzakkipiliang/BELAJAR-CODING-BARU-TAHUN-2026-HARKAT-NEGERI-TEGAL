// Hello World

console.log ("Hello World")

console.log ("\n --- batas --- \n")



// Variabel dasar

var a = "Hello World"
console.log ("A =", a)

var b = 12
console.log ("B =", b)

var c = 12.12
console.log ("C =", c)

var d = true
console.log ("d =", d)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.12
var cek = true

var tipe = `
- Teks      : ${teks}
- Angka     : ${angka}
- Cek       : ${cek}
- Desimal   : ${desimal}
`

console.log (tipe)

console.log ("\n --- batas --- \n")



// Fungsi dengan operator dasar

var x = 3
var y = 9

function tambah (x, y) {
    return x + y
}

function kurang (x, y) {
    return x - y
}

function kali (x, y) {
    return x * y
}

function bagi (x, y) {
    return x / y
}

function pangkat (x, y) {
    return x ** y
}

function modulus (x, y) {
    return x % y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Bagi =", bagi (x, y))
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")



// Percabangan dasar

var f = 9

if (f >= 8) {
    console.log (`besar, angka f = ${f}`)
}

else {
    console.log (`kecil, angka f = ${f}`)
}

console.log ("\n --- batas --- \n")



// Percabangan lanjutan 

var r = 9

if (r >= 5) {
    console.log (`besar, angka r = ${r}`)
}

else if (r >= 4) {
    console.log (`sedang, angka r = ${r}`)
}

else {
    console.log (`kecil, angka r = ${r}`)
}

console.log ("\n --- batas --- \n")




// Percabangan Nested 

var f = 2
var cek = true

if (f >= 9) {
    if (cek) {
        console.log (`besar, angka f = ${f}`)
    }

    else {
        console.log (`Sedang, angka f = ${f}`)
    }
}

else {
    console.log (`kecil, angka f = ${f}`)
}


console.log ("\n --- batas --- \n")




// For dasar

for (a = 0; a < 11; a++) {
    console.log (`urutan ke - ${a}`)
}

console.log ("\n --- batas --- \n")



for (k = 0; k < 10; k++) {
    console.log (`urutan ke - ${k}`)
}

console.log ("\n --- batas --- \n")



// Array 

var oshi = [
    "Gracie JKT48",
    "Michie JKT48",
    "Fritzy JKT48",
    "Lily JKT48",
]

oshi.push ("Lana JKT48")
oshi.push ("Erine JKT48")
oshi.push ("Delynn JKT48")

for (a = 0; a < oshi.length; a++) {
    console.log (oshi [a])
}

console.log ("\n --- batas --- \n")




// Struktur data

var data = {
    "nama" : "Habib Muzakki", 
    "kelas" : "1B",
    "asal" : "Kota Serang, Banten",
    "jurusan" : "D4 Teknik Informatika",
    "fakultas" : "Vokasi"
}

console.log ("Nama :", data ["nama"])
console.log ("Asal :", data ["asal"])
console.log ("Jurusan :", data ["jurusan"])
console.log ("Fakultas :", data ["fakultas"])

console.log ("\n --- batas --- \n")