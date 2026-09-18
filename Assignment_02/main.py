"""
main.py
Quick demo of the CampusWheels classes from rental.py.

Run with: python main.py
"""

from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    print("=== CampusWheels demo ===\n")

    # 1. Create a few vehicles and a renter, rent and return one
    car = Vehicle("Toyota", "Yaris", "1AB234")
    ecar = ElectricCar("Tesla", "Model 3", "9EV123", battery_kwh=75)
    bike = Motorbike("Honda", "Wave", "2CD567", engine_cc=125)

    renter = Renter("Somchai", 123456)

    print("Before renting:")
    print(car)

    car.rent()
    renter.rented.append(car)

    print("\nAfter renting:")
    print(car)

    car.return_vehicle()
    print("\nAfter returning:")
    print(car)

    # 2. Try to create renters with bad data and catch the errors
    print("\n=== Testing bad renter data ===")
    try:
        bad_renter = Renter("", 111)
    except ValueError as e:
        print(f"Caught expected error (empty name): {e}")

    try:
        bad_renter = Renter("Nok", -5)
    except ValueError as e:
        print(f"Caught expected error (bad license): {e}")

    # 3. Put a mix of vehicles in one list and print them
    print("\n=== All vehicles ===")
    fleet = [car, ecar, bike]
    for v in fleet:
        print(v)
        # just showing that isinstance still works for the subclasses
        print(f"  -> is a Vehicle? {isinstance(v, Vehicle)}")


if __name__ == "__main__":
    main()
