from logistics import RoadLogistics, HeavyRoadLogistics

print("===== FACTORY METHOD ROAD LOGISTICS =====")

company = input("Masukkan nama perusahaan: ")
destination = input("Masukkan tujuan pengiriman: ")
weight = int(input("Masukkan berat barang (kg): "))
distance = int(input("Masukkan jarak pengiriman (km): "))

# menentukan factory berdasarkan berat barang
if weight <= 1000:
    logistics = RoadLogistics(company)
else:
    logistics = HeavyRoadLogistics(company)

# proses pengiriman
logistics.plan_delivery(destination, distance, weight)