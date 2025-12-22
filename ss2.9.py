import sys

def Numbers(A,B,C):
    No1 = int(A)
    No2 = int(B)
    No3 = int(C)

    if(No1 > No2 and No1 > No3):
        print(f"The {No1} is greater than{No2} and {No3}")
    elif(No2 > No1 and No2 > No3):
        print(f"{No2} is greater than {No1} and {No3} ")
    else:
        print(f"{No3} is greater than {No1} and {No2}")

def main():
    Numbers(sys.argv[1],sys.argv[2],sys.argv[3])
    
if __name__ == "__main__":
    main()