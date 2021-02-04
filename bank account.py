class Bank:
    def __init__(self,name):
        self.name=name
        self.balance=0
    def deposit(self):
        amount=int(input(f"Dear {self.name},Enter the amount that to be  deposit : "))
        self.balance=self.balance+amount
        print(f"-->{amount} deposited successfully....")
        print("Dear ",self.name,", Available balance is :",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount that to be withdraw : "))
        if self.balance<amount:
            print(f"Dear {self.name}, Available balance is :{self.balance}")
            print("your account balance is not possible.......")
        else:
            self.balance=self.balance-amount
            print(f"{amount} withdraw ")
            print("Dear ",self.name,", Available balance is :",self.balance)
    def transfer(self,obj):
        transfer_amount=int(input(f"Dear {self.name},Enter the amount that to be  transfer : "))
        if(self.balance < transfer_amount):
            print("not sufficient balace in your account.....")
        else:
            self.balance-=transfer_amount
            obj.balance+=transfer_amount
            print(f"Amount {transfer_amount} is successfully Transferd from {self.name} account to {obj.name}")
            print("Dear ",self.name,", Available balance is :",self.balance)
    def accountbalance(self):
        print("Dear ",self.name,", Available balance is :",self.balance)
        
account=Bank("pranit")
account.deposit()
account.withdraw()
account.deposit()
account1=Bank("om")
account1.deposit()
account.transfer(account)
account1.accountbalance()
