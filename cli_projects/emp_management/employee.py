# employee.py

# Contains the employee class

class Employee:
    def __init__(self,name,id,dept):
        # instance variables
        self.name = name
        self.id = id
        self.dept = dept
        
    def __repr__(self):
        # return f"name={self.name}, id={self.id}, department={self.dept}"
        return f"{self.name: <20} {self.id: <5} {self.dept: <20}"


# self represents an instance