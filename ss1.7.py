
def Arithematic():
    Numbers = []
    No1 = int(input("Enter first number : "))

    No2 = int(input("Enter second number : "))

    No3 = int(input("Enter third number : "))

    No4 = int(input("Enter forth number : "))

    Numbers.extend([No1,No2,No3,No4])

    Ans = No1 + No2 + No3 + No4

    Result = int(Ans/len(Numbers))

    return Result

def main():
    Final = Arithematic()
    print("The average of three numbers is : ",Final)


if __name__ == "__main__":
    main()