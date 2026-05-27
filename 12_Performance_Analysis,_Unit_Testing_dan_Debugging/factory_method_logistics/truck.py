from transport import Transport

class Truck(Transport):

    def deliver(self, destination):
        print(
            f"Truck dengan plat {self.plate_number}, "
            f"dikendarai oleh {self.driver_name}, "
            f"mengirim barang berat ke {destination}."
        )

    def get_transport_type(self):
        return "Truck"