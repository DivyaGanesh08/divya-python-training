
class Employee():

  
    def calculate_salary(self):
        pass
class PermanentEmployee(Employee):
    def calculate_salary(self):
        return 50000

class ContractEmployee(Employee):
    def calculate_salary(self):
        return 30000
emp_type = input("Enter Employee Type (Permanent / Contract): ")

if emp_type.lower() == "permanent":
    emp = PermanentEmployee()
elif emp_type.lower() == "contract":
    emp = ContractEmployee()
else:
    print("Invalid Employee Type")
    exit()

print("Salary:", emp.calculate_salary())