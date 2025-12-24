def main():

    No = int(input("enter a number : "))
    a, b = 0,1
    count = 0
    while count < No :
        print(a,end = " ")
        a,b = b,a + b
        count = count + 1

if __name__ == "__main__":
    main()