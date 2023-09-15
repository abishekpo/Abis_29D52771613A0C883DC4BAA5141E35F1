class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} INR. New balance: {self.__balance} INR")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} INR. New balance: {self.__balance} INR")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account balance for {self.__account_holder_name} (Account #{self.__account_number}): {self.__balance} INR")

# Example usage:
if __name__ == "__main__":
    account = BankAccount("12345", "John Doe", 1000)

    account.display_balance()
    account.deposit(500)
    account.withdraw(200)
    account.display_balance()