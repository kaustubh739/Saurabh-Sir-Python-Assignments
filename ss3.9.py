
def main():
    No = int(input("Enter a number : "))
    count = 0
    while No > 0:
        Digit = No % 10 
        count = count + 1
        No = No // 10

    print(count)
if __name__ == "__main__":
    main()