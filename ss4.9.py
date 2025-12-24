
def main():
    No = int(input("ENter a number : "))
    ok = ""
    while No > 0:
        Digit = No % 10
        ok = ok + str(Digit)  
        No = No // 10
    print(ok)
if __name__ == "__main__":
    main()