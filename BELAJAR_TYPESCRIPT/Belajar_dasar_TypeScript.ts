// Hello World

console.log ("Hello World")

console.log ("\n --- batas --- \n")


// variabel dasar

let a : string = "Halo Dunia"
let b : number = 20
let c : number = 3.3
let d : boolean = true


let tipe_data = `
- Teks      : ${a}
- Angka     : ${b}
- Desimal   : ${c}
- Cek       : ${d}
`

console.log (tipe_data)

console.log ("\n --- batas --- \n")




// Fungsi dengan operator dasar

let x : number = 22
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

function bagi (x : number, y : number) {
    return x / y
}


console.log ("Tambah =", tambah (x, y))
console.log ("Kurang =", kurang (x, y))
console.log ("Kali =", kali (x, y))
console.log ("Pangkat =", pangkat (x, y))
console.log ("Bagi =", bagi (x, y))


console.log ("\n --- batas --- \n")




// Percabangan dasar

let angka_1 : number = 20

if (angka_1 >= 9) {
    console.log (`angka besar, angka 1 = ${angka_1}`)
}

else {
    console.log (`angka kecil, angka 1 = ${angka_1}`)
}

console.log ("\n --- batas --- \n")



// Percabangan Lanjutan

let angka_2 : number = 2

if (angka_2 >= 9) {
    console.log (`angka besar, angka 2 = ${angka_2}`)
}

else if (angka_2 >= 5) {
    console.log (`angka sedang, angka 2 = ${angka_2}`)
}

else {
    console.log (`angka kecil, angka 2 = ${angka_2}`)
}

console.log ("\n --- batas --- \n")