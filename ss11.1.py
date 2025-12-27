class Complex:

    def __init__(self,A=0,B=0):
        self.real = A
        self.imaginary = B

    def set_Data(self,A,B):
        self.real = A
        self.imaginary = B

    def show_Data(self):
        print(f"real and imaginary number is :{self.real} + {self.imaginary}i")


def main():
    obj1 = Complex(2,5)
    obj1.show_Data()

    obj2 = Complex()
    obj2.show_Data()

    obj3 = Complex()
    obj3.set_Data(9,4)
    obj3.show_Data()


if __name__ == "__main__":
    main()