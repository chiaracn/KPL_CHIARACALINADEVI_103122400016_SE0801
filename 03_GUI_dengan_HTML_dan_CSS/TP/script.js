const input = document.getElementById("textInput");

const jumlahHuruf = document.getElementById("jumlahHuruf");
const hurufBesar = document.getElementById("hurufBesar");
const hurufKecil = document.getElementById("hurufKecil");

input.addEventListener("input", hitungHuruf);

function hitungHuruf(){

let teks = input.value;

let total = teks.length;
let besar = 0;
let kecil = 0;

for(let i=0;i<teks.length;i++){

let char = teks[i];

if(char >= 'A' && char <= 'Z'){
besar++;
}

if(char >= 'a' && char <= 'z'){
kecil++;
}

}

jumlahHuruf.textContent = total;
hurufBesar.textContent = besar;
hurufKecil.textContent = kecil;

}

function toUpper(){
input.value = input.value.toUpperCase();
hitungHuruf();
}

function toLower(){
input.value = input.value.toLowerCase();
hitungHuruf();
}

function toParagraph(){

let teks = input.value.toLowerCase();

teks = teks.charAt(0).toUpperCase() + teks.slice(1);

input.value = teks;

hitungHuruf();

}