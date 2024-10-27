# employee_manager.py

# contains the creation and management of the employees based on the class written in the template

from employee import Employee

class EmployeeManager:
    def __init__(self)-> None:
        self.employees = []

    #  create methods for CRUD operations

    # method to create employee
    def create_employee(self,name, id, dept):
        new_emp = Employee(name,id,dept)
        self.employees.append(new_emp)
        print(f"Employee {name} Created.")

    # method to read a single employee
    def show_employee(self, id) -> Employee:
        for e in self.employees:
            if e.id == id:
                return e
        print("Employee Not found")
        return None
    
    # method to update the employee
    def update_employee(self, id, name=None, dept=None):
        for e in self.employees:
            if e.id == id:
                e.name = name
                e.dept = dept
        print(f"Employee {id} Updated.")

    # method to delete an Employee
    def delete_employee(self,id):
        for e in self.employees:
            if e.id == id:
                self.employees.remove(e)
                print(f"Employee {id} Deleted.")
                return
        print("Employee not found")
        return None

    # List all the employees
    def list_employees(self):
        for emp in self.employees:
            print(emp)