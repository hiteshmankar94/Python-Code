# Program which contains one lambda fucntion which accepts one parameter and return power of two

Square = lambda A : A**2

def main():
    Num = int(input("Enter the number:"))
    print(Square(Num))

if __name__ == "__main__":
    main()