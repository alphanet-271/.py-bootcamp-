# A Program that imitates a banking system
# It functions include, creating account, depositing, withdrawing, showing balance and account details

class BankAccount:
    def __init__(self, accountOwner, openingBalance=0):
        self.accountOwner = accountOwner
        self.accountBalance = openingBalance

    def depositMoney(self, amount):
        if amount > 0:
            self.accountBalance += amount
            print("Deposited:", amount)
            print("New Balance:", self.accountBalance)
        else:
            print("Please enter a valid amount to deposit.")

    def withdrawMoney(self, amount):
        if amount <= 0:
            print("Please enter a valid amount to withdraw.")
        elif amount > self.accountBalance:
            print("Not enough money in your account.")
        else:
            self.accountBalance -= amount
            print("Withdrawn:", amount)
            print("Remaining Balance:", self.accountBalance)

    def getBalance(self):
        return self.accountBalance

    def showAccount(self):
        print("Account Owner:", self.accountOwner)
        print("Current Balance:", self.accountBalance)


myAccount = BankAccount('Abdul', 1000)
print(myAccount.showAccount())
myAccount.withdrawMoney(500)
