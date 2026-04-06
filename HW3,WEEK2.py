# Create account to check user data
user = input("Create username: ")
passcode = input("Create password: ")
#ATM balance
money = 3000
#welcom statment
print("\n............Login ...............")
name = input("Enter username: ")
code = input("Enter password: ")
# Check user  login
if name == user and code == passcode:
    print("WELCOME! Login OK")
    #the avalible services
    print("1 Check  2 Add  3 Take") 
    option = input("Choose: ")
#check service
    if option == "1":
        print("Money:", money,"OMR","\n ...We are welcome for any more services... ")
#add service
    elif option == "2":
        amount = int(input("Add amount: "))
        money += amount
        print("Now:", money,"OMR\n ...We are welcome for any more services... ")
#take service
    elif option == "3":
        take = int(input("Take amount: "))
        if take <= money:
            money -= take
            print("Now:", money,"OMR\n ...We are welcome for any more services... ")
        else:
            print(" SORRY! Not enough money")

    else:
        print("Invalid option")

else:
    print("Access wrong ,try again!")  #wrong user data

