
def main():
    No = int(input("enter a number : "))
    highest = 0
    while No > 0:
        Digit = No % 10
        if Digit > highest:
            highest = Digit
        No = No // 10
    print(highest)
if __name__ == "__main__":
    main()
