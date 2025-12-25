def SumEven(A):
    No = A
    Ans = 0
    numbers = []
    for i in range(2,No+1,2):
        Ans = i + Ans
    numbers.append(Ans)

    return numbers


def main():
    Border = "&" * 50
    Result = SumEven(10)
    print(Border)
    print(Result)
    print(Border)

if __name__ == "__main__":
    main()