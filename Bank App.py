class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account holder: {self.name}, Balance: ${self.balance}"
    

def main():
    print("Welcome to the Bank!")
    print("Create an Account to get started.")

    name = input("Enter your name: ")
    initial_balance = float(input("Enter Initial deposit amount: $"))
    account = BankAccount(name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("\n2. Withdraw")
        print("\n3. Check Balance")
        print("\n4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawl amount: $"))
            account.withdraw(amount)
        elif choice == '3':
            print(f"Your balance: ${account.get_balance()}")
        elif choice == '4':
            print("Thank You for banking with us!")
            break
        else:
            print("Invalid Choice. Please try again.")

if __name__ == "__main__":
    main()