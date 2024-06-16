class BankAccount:
    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount

        print(f"Latest Balance: {self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance += self.amount

        print(f"Latest Balance: {self.balance}")


person1 = BankAccount("Altis Dulay", 1234, 1000)

while True:
    transaction = input("Enter transaction [deposit, withdraw, exit] ")

    if transaction == "deposit":
        amount = input("Enter amount to deposit: ")
        person1.deposit(int(amount))
    elif transaction == "withdraw":
        amount = input("Enter amount to withdraw: ")
        person1.withdraw(int(amount))
    else:
        break
