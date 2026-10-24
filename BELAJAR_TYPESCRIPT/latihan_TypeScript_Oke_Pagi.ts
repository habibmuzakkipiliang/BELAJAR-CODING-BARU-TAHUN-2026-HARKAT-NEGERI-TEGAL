// Hello World

console.log ("Hello World")


console.log ("\n --- batas --- \n")




// variabel dasar

var a : string = "Halo dunia"
var b : number = 12
var c : number = 121.2
var d : boolean = true

var tipe = `
- A     : ${a}
- B     : ${b}
- C     : ${c}
- D     : ${d}
`

console.log (tipe)

console.log ("\n --- batas --- \n")


// Cek tipe data pemrograman

console.log ("A =", typeof (a))
console.log ("B =", typeof (b))
console.log ("C =", typeof (c))
console.log ("D =", typeof (d))


console.log ("\n --- batas --- \n")


// Fungsi dengan operator dasar

var x : number = 12
var y : number = 2

function tambah (x : number, y : number) {
    return x + y
}

function kurang (x : number, y : number) {
    return x - y
}

function kali (x : number, y : number) {
    return x * y
}

function pangkat (x : number, y : number) {
    return x ** y
}

function bagi (x : number, y : number) {
    return x / y
}

function modulus (x : number, y : number) {
    return x % y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Modulus =", modulus (x, y))
console.log ("Bagi =", bagi (x, y))


console.log ("\n --- batas --- \n")



// Biodata pribadi saya

let nama : string = "Habib Muzakki"
let akrab : string = "Habib"
let asal : string = "Kota Serang, Banten"
let coding : string = "HTML, CSS, JavaScript dan Python"
let tools : string = "Github, Github Pages, Vercel dan Netlify"
let hobi : string = "Ngewota JKT48 dan suka dengan Fiony JKT48 dan Gracie JKT48"


let bio = `
- Nama lengkap      : ${nama}
- Nama panggilan    : ${akrab}
- Asal              : ${asal}
- Coding            : ${coding}
- Tools             : ${tools}
- Hobi              : ${hobi}

`

console.log (bio)

console.log ("\n --- batas --- \n")



// Percabangan dasar

var angka_1 : number = 12

if (angka_1 >= 9) {
    console.log (`besar, angka 1 = ${angka_1}`)
}

else if (angka_1 >= 5) {
    console.log (`sedang,  angka 1 = ${angka_1}`)
}

else {
    console.log (`kecil, angka 1 = ${angka_1}`)
}

console.log ("\n --- batas --- \n")



// Percabangan lanjutan

var angka_2 : number = 9

if (angka_2 >= 8) {
    console.log (`besar, angka 2 = ${angka_2}`)
}

else if (angka_2 >= 5) {
    console.log (`sedang, angka 2 = ${angka_2}`)
}

else {
    console.log (`kecil, angka 2 = ${angka_2}`)
}

console.log ("\n --- batas --- \n")