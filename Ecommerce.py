class Customer:
	def __init__(self, name, email):
		self.name = name
		self.email = email
		self.purchases = []

	def purchase(self, inventory, product):
		inventory_dict = inventory.inventory
		if product in inventory_dict:
			if inventory_dict[product] > 0:
				self.purchases.append(product)
				inventory_dict[product] -= 1
			else:
				print('We are out of Stock!')	
		else:
			print("We don't have that product.")

	def print_purchases(self):
		print("The Customers has purchased")
		for item in self.purchases:
			print(item.name)

class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price

class Inventory:
	def __init__(self):
		print ("stock we Had:-")
		self.inventory = {}

	def add_product(self, product, quantity):
		if product not in self.inventory:
			self.inventory[product] = quantity
		else:
			self.inventory[product] += quantity

	def print_inventory(self):
		for key, value in self.inventory.items():
			print (key.name + ':' + str(value))
		print( )

customer =Customer('Aakash','singhaakash084@gmail.com')

print (customer.name)
print (customer.email)

laptop = Product('Laptop', 30000)	
poco = Product ('Poco', 20000)
#print (laptop.name)
#rint(laptop.price)
#print (Poco.name)
#print(Poco.price)


inventory = Inventory()
inventory.add_product(poco, 1000)
inventory.add_product(laptop, 500)

inventory.print_inventory()
print("stock left:-")
customer.purchase(inventory, laptop)
customer.purchase(inventory,poco)
inventory.print_inventory()
customer.print_purchases()




