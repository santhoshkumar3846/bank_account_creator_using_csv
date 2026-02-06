import csv
import os
class bank_account:
    def __init__(self, bank_account_number, customer_name):
        self.bank_account_number = bank_account_number
        self.customer_name = customer_name
        self.header = ["bank_account_number", "customer_name", "available_balance"]
        self.accounts_data = "bank_accounts.csv"
    def account_exist(self):
        "checking if account already exists"
        if not os.path.exists(self.accounts_data):
            return False
        with open(self.accounts_data,"r") as f:
            reader = csv.reader(f)
            next(reader, None) #skip header
            for row in reader:
                if row and row[0] == str(self.bank_account_number):
                    return True
        return False

    def account_creation(self, minimum_balance):
        file_exists = os.path.isfile(self.accounts_data)
        if self.account_exist():
            print("account already_exist")
            return False
        with open("bank_accounts.csv", 'a', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(self.header)
            writer.writerow([self.bank_account_number, self.customer_name, minimum_balance])
        print(f"user added with {self.customer_name}, with {self.bank_account_number}, and opening_balance is {minimum_balance} INR")
    def available_balance(self):
        if not os.path.exists(self.accounts_data):
            print("Accounts file doesn't exist! Create an account")
        if self.account_exist():
            with open(self.accounts_data, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
                for row in rows:
                    if row and row[0] == str(self.bank_account_number):
                        current_balance = row[2]
            print(f'current balance is {current_balance}')
            return current_balance
        else:
            print("account doesn't exist")
    def deposit_or_withdraw(self):
        amount = int(input("enter amount to withdraw: "))
        action = input("Do you want to deposit/withdraw: ")
        if not os.path.exists(self.accounts_data):
            print("Account doesn't exist! Kindly create one :)")
            return False
        if self.account_exist():
            with open(self.accounts_data, 'r') as f:
                reader = csv.reader(f)
                rows = list(reader)
            for row in rows:
                if row and row[0] == str(self.bank_account_number):
                    current_balance = int(row[2])
                    print(f"your current balance is {current_balance}")
                    if action == "withdraw":
                        if int(current_balance) < int(amount):
                            return False
                        new_balance = int(current_balance) - int(amount)
                        print(f"Withdraw successful!, current_balance is {new_balance}")
                    elif action == "deposit":
                        new_balance = current_balance + amount
                        print(f"Deposit successful!, current_balance is {new_balance}")
                    row[2] = new_balance


            with open(self.accounts_data, 'w', newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
        print("OK")

icici = bank_account(1224, "santhosh")
# icici.account_creation(2000000)
# icici.balance_withdraw()
icici.available_balance()
icici.deposit_or_withdraw()
icici.available_balance()