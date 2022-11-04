class Numbers:
    def __init__(self, value):
        self.Value = value
        self.lst = []

    def ChkPrime(self):
        i = 0
        flag = True
        for i in range(2, (self.Value // 2)+1):
            if (self.Value % i == 0):
                flag = False
                break

        if flag == True:
            print("Given number {} is Prime number".format(self.Value))
        else:
            print("Given number {} is not Prime number".format(self.Value))

    def Factors(self):
        print("Factors of {} are:".format(self.Value))
        for i in range(1, (self.Value // 2) + 1):
            if (self.Value % i == 0):
                print(i)
                self.lst.append(i)

    def Sumfactors(self):
        Sum = 0
        for i in self.lst:
                Sum += i
        return Sum

    def ChkPerfect(self):
        if self.Sumfactors() == self.Value:
            print("The given number is perfect number")
        else:
            print("The given number is not perfect number")

def main():

    obj1 = Numbers(int(input("Enter the number:")))
    obj1.ChkPrime()
    obj1.Factors()
    print("Sum of the factors is:", obj1.Sumfactors())
    obj1.ChkPerfect()

    print("-------------------------------------------------------")
    obj2 = Numbers(int(input("Enter the number:")))
    obj2.ChkPrime()
    obj2.Factors()
    print("Sum of the factors is:", obj2.Sumfactors())
    obj2.ChkPerfect()

if __name__ == "__main__":
    main()