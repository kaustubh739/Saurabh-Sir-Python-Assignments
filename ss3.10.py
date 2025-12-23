
def main():
    No = int(input("Enter a number : "))

    Ans = 0
    while No > 0:
        Digit = No % 10 
        Ans = Digit + Ans
        No = No // 10

    print(Ans)

if __name__ == "__main__":
    main()