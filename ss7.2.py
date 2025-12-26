class Time:

    def __init__(self,A=0,B=0,C=0):
        self.hour = A
        self.minutes = B
        self.seconds = C

    def set_values(self, A,B,C):
        self.hour = A
        self.minutes = B
        self.seconds = C

    def Display_values(self):
        print(f"Live Time : {self.hour} : {self.minutes} : {self.seconds:02d}")


def main():
    obj1 = Time(12,16,00)
    obj1.Display_values()

    obj2 = Time()
    obj2.set_values(12,20,00)
    obj2.Display_values()


if __name__ == "__main__":
    main()