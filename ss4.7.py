
def main():
    No = int(input("Enter a number : "))
    binary = ""
    while No > 0:
        reminder = No % 2
        binary = str(reminder) + binary
        No = No // 2
    print(binary)

if __name__ == "__main__":
    main()