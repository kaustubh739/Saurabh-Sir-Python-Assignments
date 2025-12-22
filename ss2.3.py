def Octal():
    No = int(input("Enter a number : "))

    if((No / 8) == 0):
        print("The given number is Octal. ")
    else:
        print("It's not an octal number.")

def main():
    Octal()

if __name__ == "__main__":
    main()