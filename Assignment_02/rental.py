"""
rental.py
CampusWheels vehicle-rental desk - classes for vehicles and renters.

Assignment 2 - Advanced Computer Programming with Generative AI
"""


class Vehicle:
    """Base class for anything the desk can rent out."""

    def __init__(self, make, model, plate):
        self.make = make
        self.model = model
        self.plate = plate
        self.is_rented = False

    def rent(self):
        """Mark the vehicle as rented."""
        self.is_rented = True

    def return_vehicle(self):
        """Mark the vehicle as available again."""
        self.is_rented = False

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return f"{self.make} {self.model} ({self.plate}) [{status}]"


class ElectricCar(Vehicle):
    """An electric car - same as a Vehicle, plus a battery size."""

    def __init__(self, make, model, plate, battery_kwh):
        super().__init__(make, model, plate)
        self.battery_kwh = battery_kwh

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return (f"{self.make} {self.model} ({self.plate}) [{status}] "
                f"- Electric, {self.battery_kwh}kWh battery")


class Motorbike(Vehicle):
    """A motorbike - same as a Vehicle, plus engine size in cc."""

    def __init__(self, make, model, plate, engine_cc):
        super().__init__(make, model, plate)
        self.engine_cc = engine_cc

    def __str__(self):
        status = "rented" if self.is_rented else "available"
        return (f"{self.make} {self.model} ({self.plate}) [{status}] "
                f"- Motorbike, {self.engine_cc}cc engine")


class Renter:
    """
    A member who can rent vehicles.

    name and license_no are kept private and checked through
    properties, so they can never be set to something invalid -
    not on creation, and not later either.
    """

    def __init__(self, name, license_no):
        # this goes through the property setters below, so bad
        # values are rejected right away, even at construction time
        self.name = name
        self.license_no = license_no
        self.rented = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not value.strip():
            raise ValueError("Renter name cannot be empty.")
        self._name = value

    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        if value <= 0:
            raise ValueError("License number must be a positive number.")
        self._license_no = value

    def __str__(self):
        return f"Renter: {self.name} (license #{self.license_no})"
