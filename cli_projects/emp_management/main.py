# main py

# the file that initiates the application

from employee_manager import EmployeeManager

def main():
    new_employee = EmployeeManager()

    # creates an infinite loop
    # use a break staement to exit the loop
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
            while True:
                try:
                    emp_id = int(input("Enter Employee ID: "))
                    break
                except ValueError:
                    print("Enter a number")
            emp_name = input("Enter Employee Name: ")
            emp_dept = input("Enter the Department: ")
            new_employee.create_employee(emp_name,emp_id,emp_dept)
        elif option == 2:
            while True:
                try:
                    emp_id = int(input("Enter the Employee's id to Update: "))
                except ValueError:
                    print("Enter a number")
            if new_employee.emp_present(emp_id):
                emp_name = input("Enter the New Employee Name: ")
                emp_dept = input("Enter the New Department: ")
                new_employee.update_employee(emp_id,emp_name,emp_dept)
            else:
                print("Employee Not found")
        elif option == 3:
            while True:
                try:
                    emp_id = int(input("Enter the Employee's id to Delete: "))
                except ValueError:
                    print("Enter a number")

            new_employee.delete_employee(emp_id)
        elif option == 4:
            while True:
                try:
                    emp_id = int(input("Enter the Employee's id: "))
                except ValueError:
                    print("Enter a number")

            e = new_employee.show_employee(emp_id)
            if e:
                print(e)
        elif option == 5:
            print("---------Employee List--------")
            new_employee.list_employees()
        elif option == 6:
            print("Thanks for Using the System...........")
            break
        else:
            print("Invalid Option, please select a right one") 

if __name__ == "__main__":
    main()