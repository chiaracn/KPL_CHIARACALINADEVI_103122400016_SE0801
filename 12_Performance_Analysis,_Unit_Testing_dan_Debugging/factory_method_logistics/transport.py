from abc import ABC, abstractmethod

class Transport(ABC):

    def __init__(self, plate_number, driver_name, capacity_kg):
        self.plate_number = plate_number
        self.driver_name = driver_name
        self.capacity_kg = capacity_kg

    @abstractmethod
    def deliver(self, destination):
        pass

    @abstractmethod
    def get_transport_type(self):
        pass

    def load_cargo(self, weight_kg):
        return weight_kg <= self.capacity_kg