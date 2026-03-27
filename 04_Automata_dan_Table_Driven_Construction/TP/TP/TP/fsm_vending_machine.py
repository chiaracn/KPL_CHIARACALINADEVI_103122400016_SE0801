# fsm_vending_machine.py

# FSM menggunakan dictionary
fsm = {
    "Idle": {
        "masukkan_uang": "MenungguProduk"
    },
    "MenungguProduk": {
        "pilih_produk": "MengeluarkanProduk",
        "reset": "Idle"
    },
    "MengeluarkanProduk": {
        "keluarkan_produk": "Selesai"
    },
    "Selesai": {
        "reset": "Idle"
    }
}


def proses_fsm(event_list):
    state = "Idle"
    print(f"State awal: {state}")

    for event in event_list:
        if event in fsm[state]:
            state = fsm[state][event]
            print(f"Event: {event} -> State sekarang: {state}")
        else:
            print(f"Event: {event} tidak valid dari state {state}")

    print(f"State akhir: {state}")


# Contoh penggunaan
if __name__ == "__main__":
    print("=== Simulasi 1 ===")
    events1 = ["masukkan_uang", "pilih_produk", "keluarkan_produk"]
    proses_fsm(events1)

    print("\n=== Simulasi 2 ===")
    events2 = ["masukkan_uang", "reset"]
    proses_fsm(events2)

    print("\n=== Simulasi 3 ===")
    events3 = ["pilih_produk"]
    proses_fsm(events3)