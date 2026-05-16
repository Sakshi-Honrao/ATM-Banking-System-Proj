accounts={101: {"name": "Sakshi", "balance": 5000, "pin": 1234},
    102: {"name": "Neha", "balance": 7000, "pin": 5678}}

while True:

        print("======ATM SYSTEM=======")
        acc_no=int(input("Enter your account number: "))
        pin=int(input("Enter your PIN: "))

        if acc_no in accounts and accounts[acc_no]["pin"]==pin:
            print("Login Successful")

            while True:
                print("""
                1. Check Balance
                2. Deposit
                3. Withdraw
                4. Account Details
                5. Exit
                """)

                choice=int(input("Enter your choice: "))

                if choice==1:

                    print("Balance:",accounts[acc_no]["balance"])

                elif choice==2:

                    amount=int(input("Enter your amount: "))
                    accounts[acc_no]["balance"]+=amount

                    print("Balance Deposit Successfully")

                elif choice==3:

                    amount=int(input("Enter your amount: "))

                    if amount<=accounts[acc_no]["balance"]:
                        accounts[acc_no]["balance"]-=amount
                        print("please collect cash")
                    else:
                         print("Insufficient Balance")

                elif choice==4:

                     print("===Account Details====")

                     print("name:",accounts[acc_no]["name"])
                     print("balance:",accounts[acc_no]["balance"])

                elif choice==5:

                    print("Thank you")
                    break

                else:
                    print("Invalid Choice")

        else:
            print("Invalid Account Number or PIN")

