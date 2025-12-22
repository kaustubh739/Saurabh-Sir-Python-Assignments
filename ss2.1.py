
def Division():
    No = int(input("Enter a number : "))

    if((No % 7) == 0):
        print("Given number is divisible by 7.")
    else:
        print("Number is not divisible by 7.")

def main():
    Division()

if __name__ == "__main__":
    main()