def Odd(A):
    No = A
    numbers = []
    for i in range(1,No+1,2):
        numbers.append(i)
    return numbers

def main():
    Result = Odd(10)
    print(Result)

if __name__ == "__main__":
    main()