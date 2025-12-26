class Employee:

    def __init__(self, A,B,C):
        self.EmpId = A
        self.Empname = B
        self.EmpSalary = C

    def DisplayEmployees(Employees):
        print("\nEmployee List : ")
        for emp in Employees:
            emp.showEmployee()
        
    def sortEmployeesBySalary(self):

    def sortEmployeesByName(self):

    def sortEmployeesByEmpId(self):


def main():

    Employees = [
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000),
        Employee(101,"Kaustubh",100000) 
    ]

    Obj = Employee
    obj.DisplayEmployees(Employees)


if __name__ == "__main__":
    main()