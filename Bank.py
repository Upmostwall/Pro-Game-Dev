class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"deposited: {amount}")
        print(f"Current Balance: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent Funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Current Balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)