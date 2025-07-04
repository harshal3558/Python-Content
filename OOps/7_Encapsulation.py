## Encapsulation --> Wrapping data and functions into a single unit (object) .

## Practice

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    # Debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,'was debited')
        print('Total balance =',self.get_balance())

    # Credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,'was credited')
        print('Total balance =',self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,1234)
# print(acc1.balance)
# print(acc1.account_no)

acc1.debit(1000)
acc1.credit(500)