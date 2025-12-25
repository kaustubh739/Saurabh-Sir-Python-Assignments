def Evenatural(A):
    No = A
    numbers = []
    for i in range(2,No+1,2):
        numbers.append(i)
    return numbers

def main():
    Result = Evenatural(10)
    print(Result)

if __name__== "__main__":
    main()