import sys
Ans = 0
def Addition(No1,No2):
    Ans = No1 + No2
    return Ans

def main():
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])

    Result = Addition(number1,number2)
    print("Addition of two numbers is : ",Result)

if __name__ == "__main__":
    main()