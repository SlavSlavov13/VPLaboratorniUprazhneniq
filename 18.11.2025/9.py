class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: Balance cannot be negative.")
        else:
            self.__balance = value

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Error")

def execute_operations(account, operations):
    for op_type, amount in operations:
        if op_type == "deposit":
            account.deposit(amount)
        elif op_type == "withdraw":
            account.withdraw(amount)
    print(account.balance)

acc = BankAccount(100)
ops = [("deposit", 50), ("withdraw", 30), ("withdraw", 200)]
execute_operations(acc, ops)