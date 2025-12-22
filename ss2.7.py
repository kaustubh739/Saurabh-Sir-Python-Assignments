import sys

def EvenOdd(A):
    No = int(A)

    if((No % 2) == 0):
        print("Given number is Even")
    else:
        print("The number is Odd")

def main():
    EvenOdd(sys.argv[1])

if __name__ == "__main__":
    main()