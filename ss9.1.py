class Account:
    ROI = 7.5

    def __init__(self,A=0,B=0):
        self.Account_No = A
        self.Balance = B

    def set_Balance(self,B):
        self.Balance = B

    def set_Account_No(self,A):
        self.Account_No = A

    def get_Balance(self):
        print(f"Available balance is : {self.Balance}")

    def get_Account_No(self):
        print(f"Account number is : {self.Account_No}")

    @classmethod
    def set_ROI(cls,new_roi):
        cls.ROI = new_roi
        
    @classmethod
    def get_ROI(cls):
        print(f"ROI is : {cls.ROI}")

def main():
    obj1 = Account(101,25000)
    obj1.set_Balance(25000)
    obj1.get_Balance()

    obj2 = Account(101,25000)
    obj2.set_Account_No(101)
    obj2.get_Account_No()

    Account.get_ROI()
    Account.set_ROI(8.0)
    Account.get_ROI()

if __name__ == "__main__":
    main()