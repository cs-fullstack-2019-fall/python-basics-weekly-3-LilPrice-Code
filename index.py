# All varibles being used
balance = 0
menu = 0
deposit = 0
withdraw = 0
# challenge variables (and challange part 1
account = input("What is your name?\n")
pin = int(input("Set up a pin number?\n"))
mmenu = 0
# Seperated each menu action to better see what is going on right then while running code (plus it looks better going through the menu)
print("-----------------------------------------------------------------------")
while menu != 4:
    # Ask user it pick an option
    menu = int(input(f"Hello, {account} please choose one of following options:\n1) Check balance \n2) Add money to account \n3) Withdraw money from account \n4) Quit \nWhat will you like to do? \n"))
    # Option 1
    # Check Balance
    if menu == 1:
        print("-----------------------------------------------------------------------")
        # Printing Balance with pause to view balance without menu pushing it off the screen
        print(f"{account}'s account has ${balance} dollars.")
        send = input("Press enter to exit.")
        print("-----------------------------------------------------------------------")
    # Option 2
    # Adding money to balance
    elif menu == 2:
        print("-----------------------------------------------------------------------")
        # Loops deposit amount if below 0
        while deposit <= 0:
            deposit = int(input("How much money do you want to deposit?\n"))
            if deposit >= 0:
                balance = balance + deposit
        # Print deposit plus pause and reset deposit loop
        print(f"{account} deposited ${deposit} in your account.")
        print(f"{account}'s new balance is ${balance}")
        send = input("Press enter to exit.")
        deposit = 0
        print("-----------------------------------------------------------------------")
    # Option 2
    # Withdrawing from balance plus Challenge
    elif menu == 3:
        print("-----------------------------------------------------------------------")
        # pin loop reset
        mmenu = 0
        while mmenu == 0:
            pinch = int(input(f"Please enter your pin Number {account}\n"))
            if pinch == pin:
                # breaking pin loop
                mmenu = 1
                while withdraw <= 0:
                    print("-----------------------------------------------------------------------")
                    withdraw = int(input("How much money do you want to withdraw?\n"))
                    # Print withdraw plus pause and reset withdraw loop
                    if withdraw > 0 and withdraw < balance or withdraw == 0:
                        balance = balance - withdraw
                        print(f"{account}'s withdrawed ${withdraw}.")
                        print(f"{account}'s new balance is ${balance}.")
                        send = input("Press enter to exit.")
                        print("-----------------------------------------------------------------------")
                        ### No need to break as code in below blocks will be skipped by conditional block.
                        ### You DO NOT want to set withdraw amt back to zero as your while loop is based on that condition.
                        # withdraw = 0
                        # break
                    # Stoping over withdrawing from happening
                    elif withdraw > balance:
                        print("Insufficient funds")
                        print(f"{account}'s balance is ${balance}.")
                        send = input("Press enter to exit.")
                        print("-----------------------------------------------------------------------")
                        ### Same here as above
                        # withdraw = 0
                        # break
            elif pinch != pin:
                send = 0
                # Pim Try again loop
                while send  == 0:
                    print("-----------------------------------------------------------------------")
                    print("INCORRECT PIN")
                    send = int(input("1.EXIT \n2.TRY AGAIN\n"))
                    print("-----------------------------------------------------------------------")
                    # Give up on pin
                    if send == 1:
                        mmenu = 1
                        send = 1
                    # Trying pin again
                    elif send == 2:
                        mmenu = 0
                        send = 1
                    else:
                        ("Invalid Answer")
    # Option 4
    # The GoodBye
    elif menu == 4:
        print(f'Thank you {account} for Banking with us.')
