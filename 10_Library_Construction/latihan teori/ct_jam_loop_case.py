import time
import random
from time import time

data = [random.randint(1, 10000) for _ in range(1000000)]
        
def hitung_manual_unik(data):
            unik = []
            for item in data:
                if item not in unik:
                    unik.append(item)
            return len(unik)

start_time = time()
hitung_manual_unik = hitung_manual_unik(data)
print(f"Jumlah elemen unik: {hitung_manual_unik}")
end_time = time()
print(f"Waktu eksekusi: {end_time - start_time} detik")