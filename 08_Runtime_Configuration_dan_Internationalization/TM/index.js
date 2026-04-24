require('dotenv').config();
const axios = require('axios');

// HAPUS pesan promo dotenv
process.removeAllListeners('warning');

async function getKurs(rupiah) {
    try {
        const response = await axios.get(process.env.BASE_API);

        const rates = response.data.rates;

        const cny = rates.CNY;
        const eur = rates.EUR;

        const hasilCNY = rupiah * cny;
        const hasilEUR = rupiah * eur;

        // Format mata uang
        const formatRupiah = new Intl.NumberFormat('id-ID', {
            style: 'currency',
            currency: 'IDR'
        }).format(rupiah);

        const formatCNY = new Intl.NumberFormat('zh-CN', {
            style: 'currency',
            currency: 'CNY'
        }).format(hasilCNY);

        const formatEUR = new Intl.NumberFormat('de-DE', {
            style: 'currency',
            currency: 'EUR'
        }).format(hasilEUR);

        // Format tanggal
        const tanggal = new Intl.DateTimeFormat('id-ID', {
            dateStyle: 'full',
            timeStyle: 'medium'
        }).format(new Date());

        console.log(`Kurs ${formatRupiah} pada ${tanggal}`);
        console.log(`= ${formatCNY} dan ${formatEUR}`);
        console.log('----------------------------');

    } catch (error) {
        console.log('Terjadi error:', error.message);
    }
}

// TEST SESUAI SOAL
getKurs(25000);
getKurs(50000);
getKurs(100000);