def SimpleInterest(X,Y,Z):
    principal = X
    ROI = Y
    Time = Z

    Result = (principal * ROI * Time) / 100

    return Result

def main():
    Final = SimpleInterest(500000,7.8,2)
    print("The Simple interest is : ",Final)


if __name__ == "__main__":
    main()