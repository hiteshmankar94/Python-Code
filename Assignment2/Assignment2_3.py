# Program which accept one number from user and return its factorial

def Factorial(num):
    fact = 1

    while num != 0:
        fact = fact * num
        num -= 1
    return fact

def main():
    ino = int(input("Enter the number to find factorial:"))
    print(Factorial(ino))

if __name__ == "__main__":
    main()