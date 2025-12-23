
def main():
    No = int(input("Enter a number : "))
    ok = 0
    for i in range(1,No+1):
        Ans = (i*i)
        ok = Ans + ok

    print(ok)

if __name__ == "__main__":
    main()