// Hello World

console.log ("Hello World")

console.log ("\n --- batas --- \n")



// variabel

var a = "Halo Dunia"
console.log  ("A =", a)

var b = 12
console.log ("B =", b)

var c = 12.12
console.log ("C =", c)

var d = true
console.log ("D =", d)

console.log ("\n --- batas --- \n")



// tipe data

var teks = "Halo Indonesia"
var angka = 12
var desimal = 12.12
var cek = true

var tipe = `
- Teks  : ${teks}
- Angka  : ${angka}
- Desimal : ${desimal}
- Cek     : ${cek}
`

console.log (tipe)

console.log ("\n --- batas --- \n")



// Cek Tipe data

console.log (typeof (teks))
console.log (typeof (angka))
console.log (typeof (desimal))
console.log (typeof (cek))


console.log ("\n --- batas --- \n")



// Operator dasar

var x = 12
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

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Bagi =", bagi (x, y))
console.log ("Pangkat =", pangkat (x, y))


console.log ("\n --- batas --- \n")



// Operator perbandingan

console.log ("Hasil =", x < y)
console.log ("Hasil =", x > y)
console.log ("Hasil =", x >= y)
console.log ("Hasil =", x <= y)
console.log ("Hasil =", x == y)
console.log ("Hasil =", x != y)


// Error Handling

try {
    var a = 10 + 10
    console.log (a)
}

catch (Error) {
    console.log ("Error")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// Error Handling 1

try {
    var u = l + 0
    console.log (u)
}

catch (Error) {
    console.log ("Error")
}

finally {
    console.log ("Selesai")
}


console.log ("\n --- batas --- \n")



// Error Handling

try {
    var h = 10 + r
}

catch (Error) {
    console.log ("Error")
}

finally {
    console.log ("Selesai")
}

console.log ("\n --- batas --- \n")