# main py

# the file that initiates the application

from employee_manager import EmployeeManager

def main():
    new_employee = EmployeeManager()

    while True:
        print("----- Employee Management System--------------")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Show Employee Details")
        print("5. List All Employees")
        print("6. Exit")

        option = int(input("Select a choice from the Menu "))

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            print("Thanks for Using the System...........")
            break

if __name__ == "__main__":
    main()