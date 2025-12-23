import sys

def Addition(No):
        No = int(No)
        #No = int(input("Enter a number : "))
        Ans = 0
        for i in range(1,No+1):
            Ans = i + Ans

        print(f"Sum of first {No} numbers is : {Ans}")
            

Addition(sys.argv[1])