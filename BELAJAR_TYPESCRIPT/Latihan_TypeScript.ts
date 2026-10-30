// hello world

console.log ("Hello World")


console.log ("\n --- batas --- \n")


// Biodata pribadi saya

var nama : string = "Habib Muzakki"
var kelas : string = "1B"
var asal : string = "Kota Serang, Banten"
var coding : string = "HTML, CSS, JavaScript dan Python"
var tools : string = "Github, Github Pages, Vercel dan Netlify"


var bio = `
- Nama lengkap  : ${nama}
- Asal          : ${asal}
- Coding        : ${coding}
- Tools         : ${tools}


`

console.log (bio)

console.log ("\n --- batas --- \n")




// variabel dasar

var a : string = "Halo Dunia"
var b : number = 12
var c : number = 12.12
var d : boolean = true

var tipe = `
- A     : ${a}
- B     : ${b}
- C     : ${c}
- D     : ${d}

`

console.log (tipe)


console.log ("\n --- batas --- \n")



// fungsi dengan operator dasar

var x : number = 12
var y : number = 4

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

function modulus (x : number, y : number) {
    return x % y
}

function bagi (x : number, y : number) {
    return x / y
}

console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Modulus =", modulus (x, y))
console.log ("Bagi =", bagi (x, y))
console.log ("Pangkat =", pangkat (x, y))


console.log ("\n --- batas --- \n")



// Percabangan dasar

let ani : number = 12

if (ani >= 8) {
    console.log (`besar, angka ani = ${ani}`)
} 

else if (ani >= 5) {
    console.log (`sedang, angka ani = ${ani}`)
}

else {
    console.log (`kecil, angka ani = ${ani}`)
}

console.log ("\n --- batas ---- \n")




// Percabangan lanjutan

let anu : number = 3

if (anu >= 8) {
    console.log (`besar, angka anu = ${anu}`)
}

else if (anu >= 5) {
    console.log (`sedang, angka anu = ${anu}`)
}

else {
    console.log (`kecil, angka anu = ${anu}`)
}

console.log ("\n --- batas --- \n")



// Percabangan Nested
 
var fun : number = 12
var cek : boolean = true

if (fun >= 9) {
    if (cek) {
        console.log (`besar, angka fun = ${fun}`)
    }

    else {
        console.log (`sedang, angka fun = ${fun}`)
    }
}

else {
    console.log (`kecil, angka fun = ${fun}`)
}

console.log ("\n --- batas --- \n")



// Fungsi dengan percabangan dasar

function dasar (x : number) {

    if (x >= 6) {
        console.log (`besar, angka x = ${x}`)
    }

    else {
        console.log (`kecil, angka x = ${x}`)
    }
}

dasar (10)
dasar (9)
dasar (8)
dasar (7)
dasar (6)
dasar (5)
dasar (4)
dasar (3)
dasar (2)
dasar (1)

console.log ("\n --- batas --- \n")