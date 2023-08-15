# Description: A Program Designed for HAB Taxi Services
# Main Menu created by: John Limon
# Option 1 created by: Jelliebeth Sevilla
# Option _ created by:
# Option _ created by:
# Option _ created by:
# Written date: August 18, 2023


import option_one
import financial_listing
import car_status


# Main menu program

while True:
    print()
    print("    HAB Taxi Services    ")
    print("    Company Services System                    ")
    print()
    print(" 1. Enter a New Employee (driver). ")
    print(" 2. Enter Company Revenues. ")
    print(" 3. Enter Company Expenses. ")
    print(" 4. Track Car Rentals.")
    print(" 5. Record Employee Payment. ")
    print(" 6. Print Company Profit Listing.")
    print(" 7. Print Driver Financial Listing.")
    print(" 8. Your report - add description here")
    print(" 9. Quit Program.")
    print()

# Gathering and validating the users inputted option.

    while True:
        try:
            Selection = int(input(" Enter choice (1-9): "))
        except:
            print(" Error - Invalid Input")
        else:
            if Selection < 1 or Selection > 9:
                print(" Error - Must be 1 to 9 ")
            else:
                break

    print()

# Determining output based on the users input.

    if Selection == 1:
        option_one.OptionOne()
    if Selection == 2:
        while True:
            print("Sorry this option is not available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 3:
        while True:
            print("Sorry this option is not available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 4:
        while True:
            print("Sorry this option is not available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 5:
        while True:
            print("Sorry this option is not available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 6:
        while True:
            print("Sorry this option is not available yet.")
            BackToMenu = input("Press enter to return to menu.")
            break
    if Selection == 7:
        financial_listing.financial_listings()

    if Selection == 8:
        status = ('available','rented')
        car_status.car_status_check(*status)


    if Selection == 9:
        print("Thanks for using this program! Have a great day!")
        break
