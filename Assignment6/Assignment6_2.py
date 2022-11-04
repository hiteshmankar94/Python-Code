class BankAccount:
    ROI = 10.5
    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self):
        self.Amount = self.Amount + int(input("Enter the amount to deposit in account of {}:".format(self.Name)))

    def Withdraw(self):
        self.Amount = self.Amount - int(input("Enter the amount to withdraw from the account of {}:".format(self.Name)))

    def CalculateInterest(self):
        Interest = 0.0
        period = int(input("Enter the time period in years:"))
        Interest = (self.Amount * BankAccount.ROI * period)/100

        print("Interest on {} amount for period of {} years is {}".format(self.Amount, period, Interest))

    def Display(self):
        print("Amount in account of {} is {}:".format(self.Name, self.Amount))

def main():
    obj1 = BankAccount("Hit", 50000)
    obj1.Deposit()
    obj1.Display()
    obj1.Withdraw()
    obj1.Display()
    obj1.CalculateInterest()
    print("-------------------------------------------------------------------")

    obj2 = BankAccount("Mankar", 40000)
    obj2.Deposit()
    obj2.Display()
    obj2.Withdraw()
    obj2.Display()
    obj2.CalculateInterest()

if __name__ == "__main__":
    main()