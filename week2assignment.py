#  data
username = "admin"
password = "1234"
balance = 500
#  login function
def login():
    while True:
        u = input("Enter username: ")
        p = input("Enter password: ")
        if u == username and p == password:
            print("Login successful!")
            break
        else:
            print("Access Denied. Try again.")

#  check balance function
def check_balance():
    print("Your current balance is:", balance, "OMR")
#  deposit money function
def deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful! New balance:", balance, "OMR")
# withdraw money function
def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful! Remaining balance:", balance, "OMR")
    else:
        print("Insufficient Balance!")

# all functions to run ATM in order
def main():
    login()
    print("1. Check Balance\n2. Deposit\n3. Withdraw")
    choice = input("Enter your choice: ")
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    else:
        print("Invalid choice!")
# start the program
main()