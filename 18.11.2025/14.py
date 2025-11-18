class Vehicle:
	def __init__(self, brand, year):
		self.brand = brand
		self.year = year

class ElectricCar(Vehicle):
	def __init__(self, brand, year, battery_capacity):
		super().__init__(brand, year)
		self.battery_capacity = battery_capacity

def describe(vehicle):
	if isinstance(vehicle, ElectricCar):
		print(f"Brand: {vehicle.brand}, Battery: {vehicle.battery_capacity}kWh")
	else:
		print(f"Brand: {vehicle.brand}, Year: {vehicle.year}")

v1 = Vehicle("Toyota", 2000)
v2 = ElectricCar("Tesla", 2023, 100)
describe(v1)
describe(v2)