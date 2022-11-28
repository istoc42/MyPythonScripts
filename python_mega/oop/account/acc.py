class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def transfer(self, amount):
        pass

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    
    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance = self.balance - amount

check = Checking("account\\balance.txt")
check.transfer(110)
check.commit()
print(check.balance)

# account = Account("account\\balance.txt")
# print(account.balance)
# account.withdraw(150)
# print(account.balance)
# account.deposit(650)
# print(account.balance)
# account.commit()
# print(account.balance)