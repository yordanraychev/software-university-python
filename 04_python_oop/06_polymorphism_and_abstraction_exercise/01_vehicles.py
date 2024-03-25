from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        ...

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        ...


class Car(Vehicle):
    CONDITIONER_ON: float = 0.9

    def drive(self, distance: float) -> None:
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel


class Truck(Vehicle):
    CONDITIONER_ON: float = 1.6
    TANK_PERCENTAGE_FILL: float = 0.95

    def drive(self, distance: float) -> None:
        consumption = (self.CONDITIONER_ON + self.fuel_consumption) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.TANK_PERCENTAGE_FILL


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
