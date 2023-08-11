# Program design - Option 1 for HAB Taxi Services
# Created by: Jelliebeth Sevilla
# Written date: August 18, 2023

import datetime
import FormatValues as FV
from time import sleep

def OptionOne():

    Today = datetime.datetime.now()

    EmpCtr = 0


    # Open the defaults file and read the values into variables

    f = open('Defaults.dat', 'r')

    NextTransNum = int(f.readline())
    NextDriverNum = int(f.readline())
    MonthlyStandFee = float(f.readline())
    DailyRentFee = float(f.readline())
    WeeklyRentFee = float(f.readline())
    HST = float(f.readline())

    f.close()

    while True:

        while True:
            EmpFirstName = input("Enter the Employee's first name (END to Quit and print employee listings): ").title()

            if EmpFirstName == "":
                print("Employee name cannot be left blank. Please re-enter.")
            else:
                break
        if EmpFirstName.upper() == "END":
            break

        while True:
            EmpLastName = input("Enter the Employee's last name name: ").title()

            if EmpLastName == "":
                print("Employee last name cannot be left blank. Please re-enter.")

            else:
                break

        while True:
            EmpAdd = input("Enter the Employee's address: ")
            if EmpAdd == "":
                print("Employee address cannot be left blank. Please re-enter.")
            else:
                break

        while True:
            EmpCity = input("Enter the Employee's city: ")
            if EmpCity == "":
                print("Employee city cannot be left blank. Please re-enter.")
            else:
                break

        while True:

            EmpProv = input("Enter the Employee's province: ").upper()
            if EmpProv == "":
                print("Employee province cannot be left blank. Please re-enter.")

            elif EmpProv.isdigit() is True:
                print("Employee province can only be entered in 2 letters like NL, NS etc. Please re-enter.")

            else:
                break

        while True:
            EmpPost = input("Enter the Employee's postal code (A1A1A1): ").upper()
            if EmpProv == "":
                print("Employee province cannot be left blank. Please re-enter.")
            elif len(EmpPost) != 6:
                print("Employee postal code must be 6 characters in length. Please re-enter.")
            else:
                break

        while True:
            EmpPhone = input("Enter the Employee's phone number (9999999999): ")
            if len(EmpPhone) != 10:
                print("Employees phone number must be 10 digits in length. Please re-enter.")
            else:
                break

        while True:
            EmpDriverLic = input("Enter the employee's 10 digit drivers licence number: ")
            if len(EmpDriverLic) != 10:
                print("Employee's drivers licence number must be 10 digits in length. Please re-enter.")
            elif EmpDriverLic[0].isdigit() is True:
                print("Employee's drivers licence must start with a letter. Please re-enter.")
            else:
                break

        while True:
            EmpLicExp = input("Enter the drivers licence card expiry YYYY/MM/DD: ")
            if EmpLicExp[0:3].isalpha() is True:
                print("Card expiry must start with expiry year in form of YYYY. Please re-enter.")
            elif EmpLicExp[5:6].isalpha() is True:
                print("Card expiry month must be entered with digits only. Please re-enter")
            elif EmpLicExp[8:9].isalpha() is True:
                print("Card expiry day must be entered with digits only. Please re-enter. ")
            else:
                break

        while True:
            EmpInsurComp = input("Enter the employee's insurance provider: ")
            if EmpInsurComp == "":
                print("Employee insurance company cannot be left blank. Please re-enter.")
            else:
                break

        while True:
            InsurPolicyNum = input("Enter the employee's 8 digits insurance policy number (99999999): ")
            if InsurPolicyNum == "":
                print("Insurance policy cannot be left blank. Please re-enter.")
            elif len(InsurPolicyNum) != 8:
                print("Insurance Policy number must be 8 digits in length. Please re-enter.")
            else:
                break

        while True:
            RentOrOwn = input("Does the Employee rent or own the vehicle (R/O)?: ").upper()

            if RentOrOwn == "":
                print("Rent or Own field cannot be left blank. Please re-enter.")

            else:
                break

        EmpFullName = (f"{EmpFirstName} {EmpLastName}")

        EmpFullAdd = (f"{EmpAdd},{EmpCity},{EmpProv},{EmpPost}")

        f = open("Employees.dat", "a")

        f.write("{}, ".format(str(NextDriverNum)))
        f.write("{}, ".format(EmpFirstName))
        f.write("{}, ".format(EmpLastName))
        f.write("{}, ".format(EmpAdd))
        f.write("{}, ".format(EmpCity))
        f.write("{}, ".format(EmpProv))
        f.write("{}, ".format(EmpPost))
        f.write("{}, ".format(EmpPhone))
        f.write("{}, ".format(EmpDriverLic))
        f.write("{}, ".format(EmpLicExp))
        f.write("{}, ".format(EmpInsurComp))
        f.write("{}, ".format(InsurPolicyNum))
        f.write("{}\n".format(RentOrOwn))

        f.close()

        print()
        print("Saving Please Wait ...")
        sleep(2)
        print("Employee Info processed and saved.")
        print()

        EmpCtr += 1

        NextDriverNum += 1

        f = open('Defaults.dat', 'w')

        f.write("{}\n".format(str(NextTransNum)))
        f.write("{}\n".format(str(NextDriverNum)))
        f.write("{}\n".format(str(MonthlyStandFee)))
        f.write("{}\n".format(str(DailyRentFee)))
        f.write("{}\n".format(str(WeeklyRentFee)))
        f.write("{}\n".format(str(HST)))

        f.close()

    # Employee Listing

    print()
    print("HAB TAXI SERVICE")
    print(f"EMPLOYEE LISTING AS OF {FV.FDateMedium(Today):10s}")
    print()
    print("DRIVER              DRIVER                          DRIVER                              DRIVER")
    print("NUMBER               NAME                        FULL ADDRESS                        PHONE NUMBER")
    print("=" * 97)


    EmpCtr = 0

    f = open('Employees.dat', "r")

    for EmployeeDataLine in f:

        EmployeeLine = EmployeeDataLine.split(",")
        NextDriverNum = EmployeeLine[0].strip()
        EmpFirst = EmployeeLine[1].strip()
        EmpLast = EmployeeLine[2].strip()
        EmpAddress = EmployeeLine[3].strip()
        EmpCity = EmployeeLine[4].strip()
        EmpProv = EmployeeLine[5].strip()
        EmpPost = EmployeeLine[6].strip()
        EmpPhone = EmployeeLine[7].strip()
        EmpLicNum = EmployeeLine[8].strip()
        EmpLicExp = EmployeeLine[9].strip()
        InsurComp = EmployeeLine[10].strip()
        InsurPolNum = EmployeeLine[11].strip()
        RentOwn = EmployeeLine[12].strip()

        EmpCtr += 1
        EmpFullAdd = (f"{EmpAddress} {EmpCity},{EmpProv} {EmpPost}")

        print(f" {NextDriverNum:<6s} {EmpFirst:<15s} {EmpLast:<15s} {EmpFullAdd:<45s} {EmpPhone:>10s}")
    print("=" * 97)
    print(f"Total Employee's: {EmpCtr:>3d}")
    print()

    f.close()

    BackToMenu = input("Press enter to return to the main menu")