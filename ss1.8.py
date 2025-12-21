def swap():
    No1 = int(input("Enter first number : "))
    No2 = int(input("Enter second number : ")) 

    #No3 = No1
    #No1 = No2
    #No2 = No3
    No1, No2 = No2,No1

    print("The first number after swapping is : ",No1)
    print("The second number after swapping is : ",No2)

def main():
    swap()

if __name__ == "__main__":
    main()