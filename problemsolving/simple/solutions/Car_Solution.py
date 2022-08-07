#Car class

#The following program defines a class ("car") which includes the make,
#model, and year of a given car. The odometer begins at a value of 0.

class Car:
    def __init__(self, make, model, year): #missing __ on either side of init; missing self
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0 #missinng this attribute, it's called in readOdometer

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


#End of bugging assignment.
#1: Modifying attribute value directly (instance):
myNewCar.odometer = 15984
myNewCar.readOdometer()

#2: Modifying through a method:
    #Add this in class initialization:
    def updateOdometer(self, mileage):
        self.odometerReading = mileage

    #put this after class def:
myNewCar.updateOdometer(238)
myNewCar.readOdometer()

#3: Modifying incrementally thru method:
    #add this in class initialization:
    def incrementOdometer(self, miles):
        self.odometer += miles

    #put this after class def:
my_used_car = Car('subaru', 'outback','2015')
my_used_car.incrementOdometer(100)
my_used_car.readOdometer()
