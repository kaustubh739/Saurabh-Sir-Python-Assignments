import sys
class Area():
    PI = 3.14

def Circle(r1):
    Ans = Area.PI * r1**r1
    return Ans

def main():
    radius = int(sys.argv[1])
    Result = Circle(radius)
    print("Area of circle is : ",Result)



if __name__ == "__main__":
    main()