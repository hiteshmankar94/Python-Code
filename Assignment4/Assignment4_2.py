# Program which contains one lambda fucntion which accepts two parameter and return its multiplication

Multiplication = lambda A, B: A*B

def main():
    Num1 = int(input("Enter the 1st number:"))
    Num2 = int(input("Enter the 2nd number:"))
    print(Multiplication(Num1, Num2))

if __name__ == "__main__":
    main()