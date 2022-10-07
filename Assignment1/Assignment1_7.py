#Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def div_test():
    ino = int(input("Enter the number:"))
    if ino % 5 == 0:
        return True
    else:
        return False
def main():
    print(div_test())


if __name__ == "__main__":
    main()
