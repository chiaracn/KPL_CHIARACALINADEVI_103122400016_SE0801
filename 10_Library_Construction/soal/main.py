import time

data_mahasiswa = [
    {"nama": "Budi", "tugas": 80, "uts": 75, "uas": 90},
    {"nama": "Ani", "tugas": 60, "uts": 65, "uas": 70},
    {"nama": "Citra", "tugas": 90, "uts": 85, "uas": 95},
    {"nama": "Doni", "tugas": 50, "uts": 55, "uas": 60},
    {"nama": "Eka", "tugas": 75, "uts": 80, "uas": 85},
]

def validasi_nilai(nilai):
    if nilai is None:
        return False
    if not isinstance(nilai, (int, float)):
        return False
    if nilai < 0 or nilai > 100:
        return False
    return True

def hitung_nilai_akhir(mahasiswa):
    if "tugas" not in mahasiswa or "uts" not in mahasiswa or "uas" not in mahasiswa:
        raise ValueError(f"Data mahasiswa {mahasiswa.get('nama', 'Tanpa Nama')} tidak lengkap.")

    tugas = mahasiswa["tugas"]
    uts = mahasiswa["uts"]
    uas = mahasiswa["uas"]

    if not (validasi_nilai(tugas) and validasi_nilai(uts) and validasi_nilai(uas)):
        raise ValueError(f"Nilai {mahasiswa.get('nama', 'Tanpa Nama')} tidak valid.")

    nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)
    return nilai_akhir

def cek_kelulusan(nilai_akhir):
    return "Lulus" if nilai_akhir >= 70 else "Tidak Lulus"

def hitung_rata_rata_kelas(data):
    total = 0
    jumlah_mahasiswa = 0

    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa)
        total += nilai_akhir
        jumlah_mahasiswa += 1

    return total / jumlah_mahasiswa if jumlah_mahasiswa > 0 else 0

def cari_mahasiswa_lulus(data):
    mahasiswa_lulus = []
    for mahasiswa in data:
        nilai_akhir = hitung_nilai_akhir(mahasiswa)
        if cek_kelulusan(nilai_akhir) == "Lulus":
            mahasiswa_lulus.append(mahasiswa["nama"])
    return mahasiswa_lulus

def main():
    start = time.perf_counter()

    for mahasiswa in data_mahasiswa:
        try:
            nilai_akhir = hitung_nilai_akhir(mahasiswa)
            status = cek_kelulusan(nilai_akhir)
            print(f"{mahasiswa['nama']} - Nilai Akhir: {nilai_akhir:.2f} - Status: {status}")
        except ValueError as e:
            print(e)

    print(f"Rata-rata kelas: {hitung_rata_rata_kelas(data_mahasiswa):.2f}")
    print("Mahasiswa lulus:", cari_mahasiswa_lulus(data_mahasiswa))

    end = time.perf_counter()
    print(f"Waktu eksekusi: {end - start:.6f} detik")

if __name__ == "__main__":
    main()