import sys

def EvenNatural(No):
    numbers = []
    for i in range(No,1,-2):
        (numbers).append(i)
    return numbers

def main():
    No = int (sys.argv[1])
    Result = EvenNatural(No)
    print(Result)

if __name__ == "__main__":
    main()