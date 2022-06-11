from typing import Union


class Vehicle:
    def get_brand(self) -> str:
        pass

    def get_wheels_count(self) -> int:
        pass

    def get_seats_count(self) -> int:
        pass

    def get_vehicle_type(self) -> str:
        """
        Any of air, land, water
        :return:
        """
        pass

    def get_engine_type(self) -> str:
        """
        Any of petrol, diesel, gas, electric
        :return:
        """
        pass


class Car(Vehicle):
    def __init__(self, brand: str, engine_type: str, wheels_count: int = 4, seats_count: int = 5,
                 vehicle_type: str = "land"):
        self._brand = brand
        self._engine_type = engine_type
        self._wheels_count = wheels_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f"Car: {self._brand} with {self._engine_type} engine"


class Bike(Vehicle):
    def __init__(self, brand: str, wheels_count: int = 2, seats_count: int = 1,
                 vehicle_type: str = "land"):
        self._brand = brand
        self._wheels_count = wheels_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheels_count

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f"Bike: {self._brand}"


class VehicleFactory:
    def create(self) -> Vehicle:
        pass


class BMWCarCreator(VehicleFactory):
    def create(self) -> Car:
        return Car("BMW", "petrol")


class RometBikeCreator(VehicleFactory):
    def create(self) -> Bike:
        return Bike("Romet")


if __name__ == '__main__':
    vehicle_type: str = input("select vehicle type [bike, car, airplane]: ")
    vehicle_factory: Union[VehicleFactory, None] = None
    if vehicle_type.lower() == 'bike':
        vehicle_factory = RometBikeCreator()
    elif vehicle_type.lower() == 'car':
        vehicle_factory = BMWCarCreator()
    elif vehicle_type.lower() == 'airplane':
        # BoeingAirplane
        pass

    if vehicle_factory:
        vehicle: Vehicle = vehicle_factory.create()
        print(vehicle)
    else:
        print("Not implemented")
