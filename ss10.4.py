
class Operations:
    PI = 3.14

    def __init__(self,A,B,C):
        print("Inside Constructor")
        self.length = A
        self.breadth = B
        self.radius = C

    def __del__(self):
        print("Inside Destructor")

    def Area_Circle(self):
        Result = Operations.PI * self.radius * self.radius
        print(f"Area of circle is : {Result} ")

    def Area_Rectangle(self):
        Final = self.length * self.breadth
        print(f"Area of rectangle is : {Final}")


def main():

    Operations(10,20,5)

    obj1 = Operations(10,20,5)
    obj1.Area_Circle()

    obj2 = Operations(2,4,8)
    obj2.Area_Rectangle()

    del obj1
    del obj2
if __name__ == "__main__":
    main()