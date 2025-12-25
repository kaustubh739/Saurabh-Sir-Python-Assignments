
def Natural(A):
    No = A
    numbers = []
    for i in range(No,0,-1):
        numbers.append(i)
    return numbers

def main():
    Result = Natural(10)
    print (Result)

if __name__ == "__main__":
    main()