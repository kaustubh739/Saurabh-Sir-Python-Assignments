import sys

def Square(A):
    No = A
    numbers = []
    for i in range(1,No+1):
        numbers.append(i*i)
    return numbers

def main():
    No = int(sys.argv[1])
    Result = Square(No)
    print(Result)

if __name__ == "__main__":
    main()