// Switch Case 

function warna_lampu (r : string) {
    
    switch (r) {

        case "Merah":
            console.log ("Warna merah")
            break

        case "Kuning":
            console.log ("Warna kuning")
            break

        case "Hijau":
            console.log ("warna hijau")
            break
        
        defaut:
        console.log ("Semula")
    }
}

warna_lampu ("Merah")
warna_lampu ("Hijau")
warna_lampu ("Hijau")
warna_lampu ("Semula")

console.log ("\n --- batas --- \n")


// Percabangan dasar

var usia : number = 19

if (usia >= 19) {
    console.log (`besar, angka usia = ${usia}`)
}

else {
    console.log (`Kecil, usia = ${usia}`)
}

console.log ("\n --- batas --- \n")



// Percabangan lanjutan 

var random_1 : number = 12

if (random_1 >= 9) {
    console.log (`besar, angka random = ${random_1}`)
}

else if (random_1 >= 5) {
    console.log (`sedang, angka random = ${random_1}`)
}

else {
    console.log (`kecil, angka random = ${random_1}`)
}

console.log ("\n --- batas --- \n")



// Percabangan nested 1

var random_2 : number = 23
var cek : boolean = true

if (random_2 >= 9) {
    if (cek) {
        console.log (`besar, angka random 2 = ${random_2}`)
    }
    
    else if (random_2 >= 5) {
        console.log (`sedang, angka random = ${random_2}`)
    }
}

else {
    console.log (`kecil, angka random 2 = ${random_2}`)
}

console.log ("\n --- batas --- \n")


// Fungsi dengan percabangan dasar

function der (angka_2 : number) {

    if (angka_2 >= 9) {
        console.log (`besar, angka 1 = ${angka_2}`)
    }

    else if (angka_2 >= 5) {
        console.log (`sedang, angka angka 1 = ${angka_2}`)
    }

    else {
        console.log (`kecil, angka 1 = ${angka_2}`)
    }
}

der (10)
der (10)
der (9)
der (3)
der (2)
der (1)

console.log ("\n --- batas --- \n")




// Fungsi dengan percabangan dasar

function angka_3 (angka_3 : number) {

    if (angka_3 >= 9) {
        console.log (`besar, angka 3 = ${angka_3}`)
    }

    else {
        console.log (`kecil, angka 3 = ${angka_3}`)
    }
}

angka_3 (10)
angka_3 (9)
angka_3 (5)
angka_3 (3)
angka_3 (2)
angka_3 (2)
angka_3 (1)


console.log ("\n --- batas --- \n")