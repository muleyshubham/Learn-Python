#Example of global variables
#modify the global data from various functions

balance=5000
print(f"Initial Balance = {balance}")

def deposit():
    global balance
    balance = balance +1000
    print(f"Deposited the amount balance = {balance}")

def withdraw():
    global balance
    balance=balance-200
    print(f"Withdraw the amount balance = {balance}")

withdraw()
deposit()
withdraw()
deposit()