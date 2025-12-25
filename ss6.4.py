def ODD(A):
    No = A
    numbers = []
    for i in range(No-1,0,-2):
        numbers.append(i)
    return numbers


def main():
    result = ODD(10)
    print(result)


if __name__ == "__main__":
    main()