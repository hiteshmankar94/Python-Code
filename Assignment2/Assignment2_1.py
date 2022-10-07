import Arithimetic as arth

def main():
    ino1 = int(input("Enter the 1st number:"))
    ino2 = int(input("Enter the 2nd number:"))

    addition = arth.Add(ino1, ino2)
    print("Addition is:", addition)
    print()

    sub = arth.Sub(ino1, ino2)
    print("Subtraction is:", sub)
    print()

    mul = arth.Mult(ino1, ino2)
    print("Multiplication is:", mul)
    print()

    div = arth.Div(ino1, ino2)
    print("Division is:", div)
    print()

if __name__ == "__main__":
    main()