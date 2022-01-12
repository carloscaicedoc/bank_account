class BankAccount:
    
    all_accounts = []
    
    def __init__(self, int_rate = 0.05, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance += amount
        else:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        return f"Balance {self.balance}"

    def yield_interest(self):
        if(self.balance) > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def display_all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
        

customer_account1 = BankAccount(0.04, 700)
customer_account2 = BankAccount(0.07, 2000)

customer_account1.deposit(800).deposit(500).deposit(150).withdraw(950).yield_interest().display_account_info()
customer_account2.deposit(2000).deposit(2000).withdraw(300).withdraw(150).withdraw(75).withdraw(950).yield_interest().display_account_info()

print(BankAccount.display_all_balances())






    