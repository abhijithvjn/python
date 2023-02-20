# Create a Bank account with members account number, name, type of accountand balance. Write constructor and methods to deposit at the bank and withdraw an amount from the bank
class bank:
    def __init__(self):
        self.accnumbr=int(input("Enter your account number:"))
        self.name=str(input("Enter your name:"))
        self.acctype=str(input("Enter your accnt type:"))
        self.balance=0
    def deposit(self):
        amount=float(input("Enter the amount to deposit:"))
        print("The amount after deposit:")
        self.balance=self.balance+amount
    def withdraw(self):
        amount=float(input("Enter the amount to withdraw:"))
        if self.balance>= amount:
            print("The amount after withdrawal:")
            self.balance=self.balance-amount
        else:
            print("Withdrawal not possible")
        
    def display(self):
        print("\n Available balance:",self.balance)

s=bank()
while(True):
    print("\n 1:Deposit Money \n 2:Withdraw Money \n 3:Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        s.deposit()
        s.display()
    elif(ch==2):
        s.withdraw()
        s.display()
    else:
        exit(0)
