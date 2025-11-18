class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

	def __repr__(self):
		return f"{self.name}: {self.price}"

def filter_expensive(products, min_price):
	return list(filter(lambda p: p.price > min_price, products))

prods = [Product("Apple", 2), Product("Laptop", 1000), Product("Bread", 1)]
print(filter_expensive(prods, 5))