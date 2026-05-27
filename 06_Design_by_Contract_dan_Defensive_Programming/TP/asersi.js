const assert = require('assert');

function divide(a, b) {
    // cek apakah number
    assert(typeof a === 'number' && typeof b === 'number', 'Nilai harus bilangan');

    // cek tidak boleh nol
    assert(b !== 0, 'Tidak bisa pembagian dengan nol');

    return a / b;
}

// coba jalankan
const hasil = divide(10, 2);
console.log("Hasilnya adalah:", hasil);