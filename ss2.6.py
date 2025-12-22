def Number():
    No1 = int(input("Enter a first number : "))

    if(No1 > 0):
        print("The number is positive number.")
    elif(No1 < 0):
        print("The number is negative number.")
    else:
        print("The number is zero.")

def main():
    Number()


if __name__ == "__main__":
    main()