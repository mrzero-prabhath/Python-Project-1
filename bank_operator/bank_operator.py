import sys
print(sys.path)

from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Email is invalid!")
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")

def create_account():
    if not users:  # Check if there are no users in the system
        print("No users found. Please create a user first before creating an account.")
        return  # Exit the function early if no users exist
    
    # Proceed with the account creation workflow if users exist
    print("Select a user to create an account for:")
    for i, user in enumerate(users):
        print(f"{i + 1}. {user.name} ({user.email})")
    
    user_choice = int(input("Enter the number corresponding to the user: ")) - 1
    if 0 <= user_choice < len(users):
        account_type = input("Enter account type (e.g., Savings, Current): ")
        balance = float(input("Enter initial balance: "))
        
        # Create the account and add it to the selected user
        account = account(account_type, balance)
        users[user_choice].add_account(account)
        print(f"Account created for {users[user_choice].name}.")
    else:
        print("Invalid user selection.")


def deposit_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to deposit: "))  # Fixed bug
    user.accounts[acc_idx].deposit(amount)

def withdraw_money():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
    acc_idx = int(input("Select account: ")) - 1
    amount = float(input("Enter amount to withdraw: "))
    try:
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except ValueError as e:
        print(f"Error: {e}\n")

def view_transactions():
    list_users()
    idx = int(input("Select user: ")) - 1
    user = users[idx]
    for i, acc in enumerate(user.accounts):
        print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
        for tx in acc.get_transaction_history():
            print(tx)

