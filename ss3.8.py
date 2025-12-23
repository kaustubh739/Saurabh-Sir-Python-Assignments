
def main():
    No = int(input("Enter a number : "))
    Ans = 1
    for i in range(No,0,-1):
        Ans = Ans * i
    print(Ans)

if __name__ == "__main__":
    main()