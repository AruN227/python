class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.fuel_capacity = 10
        self.fuel_level = 0

    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print("Fuel tank is full.")
    
    def drive(self):
        """Simulate driving."""
        print("The car is moving.")

my_car = Car('audi', 'a4', 2016)
my_car.drive()
my_car.model = 'ba8'
my_car.drive()


s1 = {1,2,3}
s2 = {1,4,5}

print(s1.intersection(s2))
print(s1.union(s2))