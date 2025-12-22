# Compare two numbers.
def number(A,B):
    No1 = A
    No2 = B

    if(No1 > No2):
        print(f"{No1} is greater than {No2}")
    else:
        print(f"{No2} is greater than {No1}")

def main():
    number(100,11)


if __name__ == "__main__":
    main()