import unittest
from main import hitung_nilai_akhir, cek_kelulusan, validasi_nilai

class TestNilaiMahasiswa(unittest.TestCase):
    def test_hitung_nilai_akhir_budi(self):
        data = {"nama": "Budi", "tugas": 80, "uts": 75, "uas": 90}
        self.assertAlmostEqual(hitung_nilai_akhir(data), 82.5)

    def test_hitung_nilai_akhir_ani(self):
        data = {"nama": "Ani", "tugas": 60, "uts": 65, "uas": 70}
        self.assertAlmostEqual(hitung_nilai_akhir(data), 65.5)

    def test_cek_kelulusan_lulus(self):
        self.assertEqual(cek_kelulusan(70), "Lulus")

    def test_cek_kelulusan_tidak_lulus(self):
        self.assertEqual(cek_kelulusan(69.99), "Tidak Lulus")

    def test_validasi_nilai_none(self):
        self.assertFalse(validasi_nilai(None))

if __name__ == "__main__":
    unittest.main()