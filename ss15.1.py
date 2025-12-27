class Person:
    def __init__(self,name="",age=0):
        self.__name = name
        self.__age = age

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age
    
    class Employee(Person):

        def __init__(self, empid,salary):
            self.__empid = empid
            self.__salary = salary

        private : 
            self.name = A
            self.age = B

def main():


if __name__ == "__main__":
    main()