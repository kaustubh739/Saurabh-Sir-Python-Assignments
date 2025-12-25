import sys

def Factorial(A):
    No = A
    Ans = 1
    numbers = []
    for i in range(1, No+1):
        Ans = i * Ans
    numbers.append(Ans)

    return numbers

def main():
    No = int(sys.argv[1])
    Result = Factorial(No)
    print(Result)

if __name__ == "__main__":
    main()