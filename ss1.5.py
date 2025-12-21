
def Rectangle(len,bre):
    Result = len * bre
    print("Area of rectangle is : ",Result)

def main():
    length = int(input("Enter the length of a rectangle"))
    breadth = int(input("Enter the breadth of the rectangle"))

    Rectangle(length,breadth)

if __name__ == "__main__":
    main()