def SumEven(A):
    No = A
    Ans = 0
    numbers = []
    for i in range(1,No,2):
        Ans = i + Ans
    numbers.append(Ans)
    return numbers



def main():
    Result = SumEven(10)
    print(Result)

if __name__ == "__main__":
    main()
