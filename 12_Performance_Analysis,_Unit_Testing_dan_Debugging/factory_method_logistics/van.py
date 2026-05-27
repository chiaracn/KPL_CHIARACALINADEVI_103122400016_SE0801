from transport import Transport

class Van(Transport):

    def deliver(self, destination):
        print(
            f"Van dengan plat {self.plate_number}, "
            f"dikendarai oleh {self.driver_name}, "
            f"mengirim barang ke {destination}."
        )

    def get_transport_type(self):
        return "Van"