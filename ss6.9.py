def Sum(A):
    No = A
    Ans = 0
    numbers = []
    for i in range(1,No+1):
        Ans = (i * i) + Ans
    numbers.append(Ans)
    return numbers

def main():
    Result = Sum(10)
    print(Result)


if __name__ == "__main__":
    main()