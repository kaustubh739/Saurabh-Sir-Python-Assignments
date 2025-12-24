def Factorial(A):
    No = A
    Ans = 1
    for i in range(No,0,-1):
        Ans = i * Ans
    return Ans

def main():
    Result = Factorial(10)
    print(Result)


if __name__ == "__main__":
    main() 