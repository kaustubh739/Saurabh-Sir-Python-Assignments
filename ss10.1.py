class Complex:

    def __init__(self,A,B):
        self.real = A
        self.imaginary = B

    def set_Data(self,A,B):
        self.real = A
        self.imaginary = B

    def show_Data(self):
        print(f"real number is : {self.real} + {self.imaginary}i")

    def Addition(self):
        Result = self.real + self.imaginary
        return Result
    
    def Substraction(self):
        Result = self.real - self.imaginary
        return Result
    
    def Multiplication(self):
        Result = self.real * self.imaginary
        return Result


def main():
    obj1 = Complex(10,20)
    obj1.show_Data()

    obj2 = Complex(8,5)
    Final = obj2.Addition()
    print("Addition is : ",Final)

    obj3 = Complex(8,5)
    Final = obj3.Substraction()
    print("Substraction is : ",Final)

    obj4 = Complex(8,5)
    Final = obj4.Multiplication()
    print("Multiplication is : ",Final)



if __name__ == "__main__":
    main()