class BankAccount:
    """A simple bank account class."""

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if balance allows. Return True/False."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
