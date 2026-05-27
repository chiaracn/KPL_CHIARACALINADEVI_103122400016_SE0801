from abc import ABC, abstractmethod

from van import Van
from truck import Truck


class Logistics(ABC):

    def __init__(self, company_name):
        self.company_name = company_name

    @abstractmethod
    def create_transport(self):
        pass

    def calculate_cost(self, distance_km, weight_kg):
        return (distance_km * 5000) + (weight_kg * 100)

    def plan_delivery(self, destination, distance_km, weight_kg):

        print("\nMenentukan jenis kendaraan...")

        transport = self.create_transport()

        print(
            f"Driver {transport.driver_name} ditugaskan "
            f"untuk pengiriman ringan."
        )

        print("\n<==== DETAIL PENGIRIMAN =====")

        print(f"Perusahaan      : {self.company_name}")
        print(f"Jenis Kendaraan : {transport.get_transport_type()}")
        print(f"Nomor Plat      : {transport.plate_number}")
        print(f"Nama Supir      : {transport.driver_name}")
        print(f"Kapasitas       : {transport.capacity_kg} kg")
        print(f"Berat Barang    : {weight_kg} kg")

        if transport.load_cargo(weight_kg):
            print("Status Muatan   : Barang berhasil dimuat")
        else:
            print("Status Muatan   : Barang melebihi kapasitas")

        transport.deliver(destination)

        cost = self.calculate_cost(distance_km, weight_kg)

        print(f"Estimasi Biaya  : Rp {cost:,.0f}")


class RoadLogistics(Logistics):

    def create_transport(self):

        return Van(
            "B 8769 VAN",
            "Anto",
            1000
        )


class HeavyRoadLogistics(Logistics):

    def create_transport(self):

        return Truck(
            "B 6677 TRK",
            "Mansyur",
            5000
        )