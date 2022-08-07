#Debug This! Car class

#The following program defines a class ("car") which includes the make,
#model, and year of a given car. The odometer begins at a value of 0.

class Car:
    def init (self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def getDescription(self):
        """Return a neatly descriptive name."""
        longName = f"{self.year} {self.make} {self.model}"
        return longName.title()

    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} miles on it.")

myNewCar = Car('audi','a4',2020)
print(myNewCar.getDescription())
myNewCar.readOdometer()


#There are 2 bugs in this code! I've found:
