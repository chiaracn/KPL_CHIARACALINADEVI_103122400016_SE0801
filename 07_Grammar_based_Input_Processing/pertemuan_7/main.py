import json

# Compile process
# Bagian dari logika program
ip = "10.5.5.5"


# Runtime process
#  Variable/File Konfigurasi
with open("config.json", "r") as f:
    config = json.load(f) # Deserialisasi JSON ke dalam bentuk dictionary
    #  IP adlaah sebuah objek, maka config bisa diakses dengan menggunakan key "ip_address"
    ip = config["ip_address"]
    
print(ip)
