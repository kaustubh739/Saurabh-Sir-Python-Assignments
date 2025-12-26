class Complex:

    def __init__(self,A=0,B=0):
        self.real = A
        self.imaginary = B

    def set_values(self,A,B):
        self.real = A
        self.imaginary = B

    def print_values(self):

        print(f"Complex Number : {self.real} + {self.imaginary}i")

def main():
    obj1 = Complex(3,4)
    obj1.print_values()

    obj2 = Complex()
    obj2.set_values(6,2)
    obj2.print_values()

if __name__ == "__main__":
    main()
