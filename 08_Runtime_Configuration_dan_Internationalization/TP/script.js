// ambil tanggal sekarang
const sekarang = new Date();

// format sesuai Indonesia
const formatter = new Intl.DateTimeFormat('id-ID', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric'
});

// tampilkan ke HTML
document.getElementById("tanggal").innerText = formatter.format(sekarang);