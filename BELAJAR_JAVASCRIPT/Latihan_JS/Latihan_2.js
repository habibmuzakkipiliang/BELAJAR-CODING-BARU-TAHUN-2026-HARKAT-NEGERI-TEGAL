// Hello World

console.log ("Hello World")

var angka = 12
console.log ("Angka =", angka)

var teks = "Halo Dunia"
console.log ("Teks =", teks)

var cek = true
console.log ("Cek =", cek)

var tes = "Halo Dunia Indonesia"
console.log ("Tes =", tes)

var hun = "Halo Tegal"
console.log ("Hun =", hun)


console.log ("\n --- batas --- \n")



// Operator dasar

var a = 9
var b = 5

function tambah (a, b) {
    return a + b
}

function kurang (a, b) {
    return a - b
}

function kali (a, b) {
    return a * b
}

function pangkat (a, b) {
    return a ** b
}

function bagi (a, b) {
    return a / b
}

console.log ("Tambah =", tambah (a, b))
console.log ("Kurang =", kurang (a, b))
console.log ("Kali =", kali (a, b))
console.log ("Bagi =", bagi (a, b))
console.log ("Pangkat =", pangkat (a, b))


console.log ("\n --- batas --- \n")



// Operator perbandingan

console.log ("Hasil =", a > b)
console.log ("Hasil =", a < b)
console.log ("Hasil =", a <= b)
console.log ("Hasil =", a >= b)
console.log ("Hasil =", a == b)
console.log ("Hasil =", a != b)


console.log ("\n --- batas --- \n")



// Percabangan dasar
 
var a = 9

if (a >= 8) {
    console.log (`Besar, angka a = ${a}`)
}

else {
    console.log (`Kecil, angka a = ${a}`)
}


console.log ("\n --- batas --- \n")



// Percabangan dasar 2

var b = 3

if (b >= 8) {
    console.log (`Besar, angka b = ${b}`)
}

else {
    console.log (`Kecil, angka b = ${b}`)
}

console.log ("\n --- batas --- \n")



// Percabangan lain 

var y = 8

if (y >= 6) {
    console.log (`besar, angka y = ${y}`)
}

else if (y >= 5) {
    console.log (`Sedang, angka y = ${y}`)
}

else {
    console.log (`Kecil, angka y = ${y}`)
}

console.log ("\n --- batas --- \n")



// Percabangan nested

var f = 8
var cek = true

if (f >= 8) {
    if (cek) {
        console.log (`Besar, angka f = ${f}`)
    }

    else {
        console.log (`Sedang, angka f = ${k}`)
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



// For dasar 2

for (b = 1; b < 11; b++) {
    console.log (`urutan ke - ${b}`)
}


console.log ("\n --- batas --- \n")



// for dasar 4

for (u = 5; u < 11; u++) {
    console.log (`urutan ke - ${u}`)
}


console.log ("\n --- batas --- \n")



// While dasar

var f = 1

while (f < 10) {
    console.log (`urutan ke - ${f}`)
    f++
}


console.log ("\n --- batas --- \n")