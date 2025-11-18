class BankAccount:
	def __init__(self, balance):
		self.__balance = balance

	def deposit(self, amount):
		self.__balance += amount

	def withdraw(self, amount):
		if amount <= self.__balance:
			self.__balance -= amount
		else:
			print("Error")

	def get_balance(self):
		return self.__balance

def execute_operations(account, operations):
	for op_type, amount in operations:
		if op_type == "deposit":
			account.deposit(amount)
		elif op_type == "withdraw":
			account.withdraw(amount)
	print(account.get_balance())

acc = BankAccount(100)
ops = [("deposit", 50), ("withdraw", 30), ("withdraw", 200)]
execute_operations(acc, ops)