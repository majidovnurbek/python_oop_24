class BankAccount:
    total_accounts = 0

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"Name: {self.account_holder} amount:{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"sizda mablag' yetarli emas. Sizing balans {self.balance} bor")  # noqa
        print(f"Name: {self.account_holder} amount:{self.balance}")

    @classmethod
    def get_account_total(cls):
        return f"Umumiy hisoblar: {cls.total_accounts}"  # noqa

    @staticmethod
    def calculate_interest(balance, rate):
        return balance * rate / 100

    def __str__(self):
        return f"Name: {self.account_holder} Balance: {self.balance}"


# hisob ochish
account1 = BankAccount("Ali", 500)
account2 = BankAccount("Jamol", 1000)
print(account1)
print(account2)

account1.deposit(400)
account2.withdraw(500)



print(BankAccount.get_account_total())

interests = BankAccount.calculate_interest(1000, 5)
print(f"Foyiz: {interests}")
