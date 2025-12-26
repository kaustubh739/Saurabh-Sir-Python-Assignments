class Box:

    def __init__(self,A=0,B=0,C=0):
        self.length = A
        self.breadth = B
        self.height = C

    def set_Dimensions(self,A,B,C):
        self.length = A
        self.breadth = B
        self.height = C

    def Display_Dimensions(self):
        print(f"Length : {self.length},Breadth : {self.breadth},Height : {self.height}")

    def Display_volume(self):
        Result = self.length * self.breadth * self.height
        return Result

def main():
    obj1 = Box(10,20,30)
    obj1.Display_Dimensions()

    obj2 = Box()
    obj2.set_Dimensions(1,2,3)
    obj2.Display_Dimensions()

    obj3 = Box(10,5,2)
    Final = obj3.Display_volume()
    print("Volume of cuboid is : ",Final)

if __name__ == "__main__":
    main()