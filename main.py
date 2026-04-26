from display_balance import display_balance
from deposit import deposit
from withdraw import withdraw
from statement import statement

def atm():
    while True:
        print("\n" + "═" * 40)
        print("         WELCOME TO THE ATM")
        print("═" * 40)
        print("  1. Display Balance")
        print("  2. Deposit Money")
        print("  3. Withdraw Money")
        print("  4. Account Statement")
        print("  5. Exit")
        print("═" * 40)
        choice = int(input("Enter your choice: "))

        if   choice == 1: display_balance()
        elif choice == 2: deposit()
        elif choice == 3: withdraw()
        elif choice == 4: statement()
        elif choice == 5:
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

print(atm())
