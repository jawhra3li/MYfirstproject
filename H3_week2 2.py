# Login
username = "admin" #name
password = "1234" #password
balance = 500 #balance money
while True: #checking login
    u = input("Enter username: ")
    p = input("Enter password: ")
    if u == username and p == password:
        print("Login successful!")
        break 
    else:
        print("Access Denied. Try again.")
#ATM service
print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money")
choice = input("Enter your choice: ")
if choice == "1":
    print("Your current balance is:", balance, "OMR")
elif choice == "2":
    amount = int(input("Enter amount to deposit: "))
    balance += amount
    print("Deposit successful! Your new balance is:", balance, "OMR")
elif choice == "3":
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful! Your remaining balance is:", balance, "OMR")
    else:
        print("Insufficient Balance! Your current balance is:", balance, "OMR")
else:
    print("no choice found !") #if no 1,2,3 service chose

