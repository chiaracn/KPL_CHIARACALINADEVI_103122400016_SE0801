from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

def get_vehicle(vehicle_type):
    if vehicle_type == "car":
        return Car()
    elif vehicle_type == "motorcycle":
        return Motorcycle()
    else:
        raise ValueError("Invalid vehicle type")

vehicle1 = get_vehicle("car")
vehicle1.start_engine()

vehicle2 = get_vehicle("motorcycle")
vehicle2.start_engine()