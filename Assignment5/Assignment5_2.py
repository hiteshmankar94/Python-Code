class Circle:
    Pi = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius of circle:"))

    def CalculateArea(self):
        self.Area = Circle.Pi * self.Radius ** 2

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.Pi * self.Radius

    def Display(self):
        print("Area of the Circle with radius {} is: {}".format(self.Radius,self.Area))
        print("Circumference of the Circle with radius {} is: {}".format(self.Radius, self.Circumference))

def main():
    Obj1 = Circle()
    Obj2 = Circle()

    Obj1.Accept()
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2.Accept()
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__ == "__main__":
    main()