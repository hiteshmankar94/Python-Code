class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first number:"))
        self.Value2 = int(input("Enter the second number:"))

    def Addition(self):
        Sum = 0
        Sum = self.Value1 + self.Value2

        return Sum

    def Subtraction(self):
        Sub = 0
        Sub = self.Value1 - self.Value2

        return Sub

    def Multiplication(self):
        Mul = 0
        Mul = self.Value1 * self.Value2

        return Mul

    def Division(self):
        Div = 0
        Div = self.Value1 / self.Value2

        return Div

def main():
    obj1 = Arithmetic()
    obj2 = Arithmetic()

    obj1.Accept()
    print("Addition is:", obj1.Addition())
    print("Subtraction is:", obj1.Subtraction())
    print("Multiplication is:", obj1.Multiplication())
    print("Division is:", obj1.Division())

    obj2.Accept()
    print("Addition is:", obj2.Addition())
    print("Subtraction is:", obj2.Subtraction())
    print("Multiplication is:", obj2.Multiplication())
    print("Division is:", obj2.Division())

if __name__ == "__main__":
    main()