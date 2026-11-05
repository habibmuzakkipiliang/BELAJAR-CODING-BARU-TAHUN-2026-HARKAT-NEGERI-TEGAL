console.log ("Hello World")


console.log ("\n --- batas --- \n")



// Biodata lengkap Habib Muzakki

let nama : string = "Habib Muzakki"
let akrab : string = "Habib"
let asal : string = "Kota Serang, Banten"
let coding : string = "HTML, CSS, JavaScript, TypeeScript dan Python"
let hobi : string = "JKT48 dan suka oshi JKT48 yang cantik"
let kampus : string = "Universitas Harkat Negeri Tegal"
let fakultas : string = "Sekolah Vokasi"
let jurusan : string = "D4 Teknik Informatika"


let profil = `
\n Nama lengkap     : ${nama}
\n Nama panggilan   : ${akrab}
\n Asal daerah      : ${asal}
\n Coding           : ${coding}
\n Hobi             : ${hobi}
\n Kampus           : ${kampus}
\n Fakultas         : ${fakultas}
\n Jurusan          : ${jurusan}

`

console.log (profil)


console.log ("\n --- batas --- \n")



// variabel dasar

let a : string = "Halo Dunia saya yang indah"
let b : string = "Halo Saya Habib Muzakki, D4 Teknik Informatika"
let c : string = "Halo Saya ingin belajar dasar pemrograman"
let d : number = 12
let e : number = 3.12


console.log (a)
console.log (b)
console.log (c)
console.log (d)
console.log (e)


console.log ("\n --- batas --- \n")



// Percabangan dasar

let hun : number = 12

if (hun >= 5) {
    console.log (`besar, angka hun = ${hun}`)
}

else {
    console.log (`kecil, angka hun = ${hun}`)
}


console.log ("\n --- batas --- \n")



// percabangan lanjutan 

let gnu : number = 12

if (gnu >= 9) {
    console.log (`besar, angka gnu = ${gnu}`)
}

else {
    console.log (`kecil, angka gnu ${gnu}`)
}

console.log ("\n --- batas --- \n")





// Percabangan lanjutan

let jun : number = 9

if (jun >= 8) {
    console.log (`besar, angka jun = ${jun}`)
}

else {
    console.log (`kecil, angka jun = ${jun}`)
}



console.log ("\n --- batas --- \n")




// Tipe data pemrograman

let teks : string = "Halo Dunia"
let angka : number = 12
let desimal : number = 11.2
let cek : boolean = true


let tipen = `
\n - Teks       : ${teks}
\n - Angka      : ${angka}
\n - Desimal    : ${desimal}
\n - Cek        : ${cek}

`

console.log (tipen)


console.log ("\n --- batas --- \n")




// Cek tipe data pemrograman

console.log ("Teks =", typeof (teks))
console.log ("Angka =", typeof (angka))
console.log ("Desimal =", typeof (desimal))
console.log ("Cek =", typeof (cek))


console.log ("\n --- batas --- \n")



// Fungsi return dengan operator dasar

let x : number = 12
let y : number = 3

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


console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))


console.log ("\n --- batas --- \n")



// For dasar

for (let a = 0; a < 15; a++) {
    console.log (`urutan ke - ${a}`)
}


for (let b = 1; b < 20; b++) {
    console.log (`urutan ke - ${b}`)
}

for (let k = 10; k < 20; k++) {
    console.log (`urutan ke - ${k}`)
}

console.log ("\n --- batas --- \n")