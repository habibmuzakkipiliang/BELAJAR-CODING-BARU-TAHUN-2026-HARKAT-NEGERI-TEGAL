// Hello World 

console.log ("Hello World")

console.log ("\n --- batas --- \n")



// variabel dasar

var a = "Halo Dunia"
console.log ("A =", a)

var b = 12
console.log ("B =", b)

var c = 12.12
console.log ("C =", c)

var d = true
console.log ("D =", d)


console.log ("\n --- batas --- \n")



// Tipe data pemrograman

var teks = "Halo Dunia"
var angka = 12
var desimal = 12.12
var cek = true

var tipe = `
- Teks      : ${teks}
- Angka     : ${angka}
- Desimal   : ${desimal}
- Cek       : ${cek}

`

console.log (tipe)


console.log ("\n --- batas --- \n")



// Cek tipe data pemrograman 

console.log ("Teks =", typeof (teks))
console.log ("Angka =", typeof (angka))
console.log ("Desimal =", typeof (desimal))
console.log ("Cek =", typeof (cek))


console.log ("\n --- batas --- \n")



// Fungsi dalam operasi aritmatika dasar

var x = 9
var y = 4

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
console.log ("Modulus =", modulus (x, y))


console.log ("\n --- batas --- \n")




// Percabangan dasar

var t = 9

if (t >= 8) {
    console.log (`angka besar, angka t = ${t}`)
}

else if (t >= 5) {
    console.log (`angka kecil, angka t = ${t}`)
}

console.log ("\n --- batas --- \n")




// Percabangan Lanjutan

var f = 4

if (f >= 8) {
    console.log (`Angka besar, angka f = ${f}`)
}

else if (f >= 5) {
    console.log (`Angka sedang, angka f = ${f}`)
}

else {
    console.log (`Angka kecil, angka f = ${f}`)
}


console.log ("\n --- batas --- \n")



// Percabangan Cuaca Hari ini

var cuaca = "cerah"
var suhu = 20

if (cuaca == "cerah") {
    if (suhu > 30) {
        console.log ("Cerah boleh keluar rumah")
    }

    else {
        console.log ("Harus bawa topi")
    }
}

else if (cuaca == "hujan") {
    if (suhu < 30) {
        console.log ("Hujan dan dingin hari ini dan jangan keluar rumah")
    }

    else {
        console.log ("Bawa payung dan mentel hujan")
    }
}

else if (cuaca == "berawan") {
    if (suhu < 30) {
        console.log ("Berawan, boleh keluar rumah sambil lari tipis-tipe")
    }
    
    else {
        console.log ("Jangan dulu keluar")
    }
}

else {
    console.log ("Input tidak valid")
}

console.log ("\n --- batas --- \n")



// For dasar

for (a = 0; a < 11; a++) {
    console.log (`urutan ke - ${a}`)
}

for (b = 1; b < 15; b++) {
    console.log (`urutan ke - ${b}`)
}

for (c = 5; c < 20; c++) {
    console.log (`urutan ke - ${c}`)
}

console.log ("\n --- batas --- \n")



// While dasar

var a = 1

while (a < 10) {
    console.log (`urutan ke - ${a}`)
    a++
}


console.log ("\n --- batas --- \n")



var b = 10

while (b > 0) {
    console.log (`urutan ke - ${b}`)
    b--
}