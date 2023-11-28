print("="*36)
print("  ---  Welcome to Indian bank  ---")
print("*"*36)
print("=<< 1. Create a new account      >>=")
print("=<< 2. Withdraw Money            >>=")
print("=<< 3. Deposit Money             >>=")
print("=<< 4. Check Customer & Balance  >>=")
print("=<< 5. Exit/Quit                 >>=")
print("*"*36)
selection=int(input("Enter your option number from the above menu : "))
a=0
print("Option number",selection,"is selected by the client")
class BankAccount:
    def __init__(self, name, pin,balance):
        self.name = name
        self.balance = balance
        self.pin=pin
    def pin_check(self):
        return self.pin
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited in your account. New balance: {self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn from your account. New balance: {self.balance}")
        else:
            print("Insufficient funds.")
    def display_balance(self):
        print(f"Customer name is: {self.name}")
        print(f"Your current balance is: {self.balance}")               
if(selection==1):
    a+=1
    print("Number of clients :",a)
    name=input("Enter Full name : ")
    pin=int(input("Enter a pin of your choice : "))
    amt=int(input("Enter the amount of money you want to deposit to start the account : "))
    account=BankAccount(name,pin,amt)
    while(1):
        selection1=int(input("Enter your option number : "))
        if(selection1==2):
            wd=int(input("Enter the amount of money you want to withdraw : "))
            check=int(input("Enter your pin : "))
            if(account.pin_check()==check):
                account.withdraw(wd)
            else:
                print("Transaction is cancelled\nPlease Enter the correct pin")
        elif(selection1==3):
            deposit=int(input("Enter the amount of money you want to deposit : "))
            account.deposit(deposit)
            print("Thank you for your deposit :)")
        elif(selection1==4):
            account.display_balance()
        elif(selection1==5):
            print("Shuting down the banking system...")
            break;
        else:
            print("Please enter a valid option number")
elif(selection==5):
    print("Shuting down the banking system...")
elif(selection==2 or selection==3 or selection==4):
    print("Create an Account first")
else:
    print('Please enter a valid option number')
