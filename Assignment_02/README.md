# CampusWheels - Assignment 2

Simple OOP practice for Advanced Computer Programming with Generative AI.
Models a small vehicle-rental desk: `Vehicle`, `ElectricCar`, `Motorbike`,
and `Renter`.

## How to run

```
python main.py
```

This prints a short demo: renting/returning a vehicle, catching a couple
of `ValueError`s from bad renter data, and looping through a mixed list
of vehicles so you can see each `__str__` looks different.

To run the tests (if you have the test file):

```
pytest
```

## Files

- `rental.py` - all the classes
- `main.py` - demo script
- `README.md` - this file

## AI use note

I used AI (Claude) to help me understand how `@property` works in Python
and to double check that inheritance with `super().__init__()` was set
up correctly, since I wasn't 100% sure on the syntax at first. I also
asked it to explain why the check needs to be in the setter and not just
in `__init__` (so it runs every time, not only when the object is
created). I wrote and typed the actual code myself and tested it in my
own terminal before submitting.
