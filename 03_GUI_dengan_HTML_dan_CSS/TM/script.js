const editorBesar = document.getElementById("editor-besar");
const editorKecil = document.getElementById("editor-kecil");
const jumlahHurufKecil = document.getElementById("hk");
const tombolHurufBesar = document.getElementById("huruf-besar");
const tombolHurufKecil = document.getElementById("huruf-kecil");

// Fungsi menghitung jumlah huruf kecil
function hitungHurufKecil(teks) {
  let jumlah = 0;

  for (let i = 0; i < teks.length; i++) {
    const karakter = teks[i];

    if (karakter >= "a" && karakter <= "z") {
      jumlah++;
    }
  }

  return jumlah;
}

// Saat user mengetik di editor utama, jumlah huruf kecil diperbarui
editorBesar.addEventListener("input", function () {
  const teks = editorBesar.value;
  jumlahHurufKecil.textContent = hitungHurufKecil(teks);
});

// Tombol ubah ke huruf besar
tombolHurufBesar.addEventListener("click", function () {
  const teks = editorBesar.value;
  editorKecil.value = teks.toUpperCase();
});

// Tombol ubah ke huruf kecil
tombolHurufKecil.addEventListener("click", function () {
  const teks = editorBesar.value;
  editorKecil.value = teks.toLowerCase();
});