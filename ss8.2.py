class Employee:

    def __init__(self,A,B,C):
        self.empid = A
        self.name = B
        self.salary = C

    def setEmployeeId(self,A):
        self.empid = A

    def setEmployeeName(self,B):
        self.name = B
    
    def setEmployeeSalary(self,C):
        self.salary = C

    def Show_Employee(self):
        print(f"Employee details : id : {self.empid}, Name : {self.name}, Salary : {self.salary}")

    def getSalary(self):
        print(f"The Salary of employee is {self.salary}")

    def getEmpId(self):
        print(f"The Employee id is : {self.empid}")

    def getName(self):
        print(f"The employee name is : {self.name}")

def main():
    obj = Employee(101,"Kaustubh",100000)
    obj.Show_Employee()
    obj.getSalary()
    obj.getEmpId()
    obj.getName()


if __name__ == "__main__":
    main()