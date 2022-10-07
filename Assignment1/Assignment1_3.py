#Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def Add(num1, num2):
    return num1+num2

def main():
    ino1 = int(input("Enter 1st number:"))
    ino2 = int(input("Enter 2nd number:"))

    print(Add(ino1, ino2))

if __name__ == "__main__":
    main()
