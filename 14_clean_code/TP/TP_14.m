# TUGAS PENDAHULUAN 14

## Refactoring Clean Code dan Event Handling

### Nama : Chiara Calina Devi

### NIM : 103122400016

### Kelas : SE-08-01

---

# Pendahuluan

Pada tugas ini dilakukan analisis dan refaktorisasi terhadap fungsi JavaScript yang digunakan untuk menampilkan detail pesanan pada modal, mengatur tombol konfirmasi, serta menangani komunikasi dengan API. Meskipun kode awal dapat berjalan dengan baik, terdapat beberapa pelanggaran terhadap prinsip Clean Code yang menyebabkan kode sulit dipelajari, dipelihara, dan dikembangkan di masa depan.

Tujuan refaktorisasi adalah meningkatkan keterbacaan (readability), maintainability, modularitas, dan menerapkan prinsip Single Responsibility Principle (SRP).

---

# Kode Awal

Fungsi `fetchOrderDetails()` memiliki beberapa tanggung jawab sekaligus, yaitu:

1. Mengambil data dari API.
2. Menangani error.
3. Membuat elemen DOM.
4. Menampilkan modal.
5. Mengatur tombol close.
6. Mengatur tombol konfirmasi.
7. Menjalankan proses konfirmasi pesanan.

Akibatnya fungsi menjadi terlalu panjang dan sulit dipelihara.

---

# Identifikasi Permasalahan Clean Code

## 1. Single Responsibility Principle (SRP)

Satu fungsi memiliki banyak tanggung jawab.

```text
fetchOrderDetails()
├── Fetch API
├── Render UI
├── Open Modal
├── Close Modal
└── Confirm Order
```

Prinsip SRP menyatakan bahwa satu fungsi sebaiknya hanya memiliki satu alasan untuk berubah.

---

## 2. Separation of Concerns

Logika bisnis dan tampilan bercampur dalam satu fungsi.

Contoh:

```javascript
fetch(...)
```

bercampur dengan:

```javascript
document.createElement(...)
```

dan:

```javascript
confirmOrder(...)
```

Hal ini membuat proses debugging menjadi lebih sulit.

---

## 3. Event Listener Duplication

Setiap modal dibuka, event listener baru akan ditambahkan.

```javascript
closeBtn.addEventListener(...)
confirmBtn.addEventListener(...)
```

Jika modal dibuka berkali-kali, listener akan menumpuk dan menyebabkan bug.

---

## 4. Readability

Panjang fungsi yang berlebihan membuat kode sulit dibaca dan dipahami oleh developer lain.

---

# Hasil Refaktorisasi

Untuk meningkatkan kualitas kode, fungsi besar dipecah menjadi beberapa modul.

## Struktur Folder

```text
project/
│
├── index.html
│
├── js/
│   │
│   ├── api/
│   │   └── orderApi.js
│   │
│   ├── services/
│   │   └── orderService.js
│   │
│   ├── ui/
│   │   └── orderModal.js
│   │
│   └── main.js
│
└── css/
    └── style.css
```

---

# Penjelasan Setiap File

## orderApi.js

Bertanggung jawab untuk komunikasi dengan API.

```javascript
export async function getOrderDetails(orderId, token) {
    ...
}
```

Tanggung jawab:

* Mengirim request ke server.
* Memvalidasi response.
* Mengembalikan data order.

---

## orderService.js

Berisi logika bisnis aplikasi.

```javascript
export function confirmOrder(orderId, token) {
    ...
}
```

Tanggung jawab:

* Menjalankan proses konfirmasi pesanan.
* Menghubungkan frontend dengan backend.

---

## orderModal.js

Mengatur seluruh tampilan modal.

Fungsi yang tersedia:

```javascript
renderOrderDetails()
showModal()
setupCloseButton()
setupConfirmButton()
```

Tanggung jawab:

* Menampilkan informasi pesanan.
* Mengatur interaksi pengguna.
* Menampilkan dan menyembunyikan modal.

---

## main.js

Berfungsi sebagai controller.

```javascript
fetchOrderDetails()
```

Tanggung jawab:

* Menghubungkan API, Service, dan UI.

---

# Analisis Alur Sistem

## Ketika User Menekan Tombol Detail Pesanan

```text
User
  ↓
fetchOrderDetails()
  ↓
getOrderDetails()
  ↓
API Server
  ↓
Data Order Diterima
  ↓
renderOrderDetails()
  ↓
showModal()
```

---

## Ketika User Menekan Tombol Konfirmasi

```text
User
  ↓
Klik Confirm
  ↓
confirmOrder(order.id, token)
  ↓
Request ke Backend
  ↓
Update Database
  ↓
Status Pesanan Berubah
```

---

# Keunggulan Setelah Refaktorisasi

## Readability

Kode lebih pendek dan mudah dipahami.

## Maintainability

Perubahan pada API tidak memengaruhi tampilan UI.

## Reusability

Fungsi dapat digunakan kembali pada halaman lain.

## Scalability

Mudah dikembangkan untuk fitur tambahan.

## Debugging

Kesalahan lebih mudah ditemukan karena setiap file memiliki tanggung jawab yang jelas.

---

# Prinsip Clean Code yang Diterapkan

| Prinsip                         | Implementasi                             |
| ------------------------------- | ---------------------------------------- |
| Single Responsibility Principle | Setiap file memiliki satu tanggung jawab |
| Separation of Concerns          | UI, API, dan Business Logic dipisahkan   |
| Readability                     | Nama fungsi jelas dan mudah dipahami     |
| Reusability                     | Fungsi dapat digunakan kembali           |
| Maintainability                 | Mudah diperbarui dan dikembangkan        |
| Modular Programming             | Kode dipisah menjadi beberapa modul      |

---

# Kesimpulan

Refaktorisasi dilakukan untuk meningkatkan kualitas perangkat lunak dengan menerapkan prinsip-prinsip Clean Code. Kode yang sebelumnya memiliki banyak tanggung jawab dalam satu fungsi dipecah menjadi beberapa modul sesuai tugasnya masing-masing. Hasilnya adalah kode yang lebih mudah dibaca, dipelihara, diuji, dan dikembangkan pada masa mendatang.

Penerapan Single Responsibility Principle (SRP), Separation of Concerns (SoC), dan Modular Programming menjadikan struktur program lebih profesional dan sesuai dengan praktik pengembangan perangkat lunak modern.
