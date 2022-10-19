# Program which accept N number from user and store it into List and return addition of prime number from that list with module concept

from MarvellousNum import *

def ListPrime(lst1):
    Sum = 0
    for i in lst1:
        if (ChkPrime(i) == True):
            Sum += i
    return Sum

def main():
    lst = list()

    num = int(input("enter the number of elements:"))
    print("Enter the {} elements".format(num))

    for i in range(num):
        lst.append(int(input()))

    print("Addition of Prime numbers in list is:", ListPrime(lst))

if __name__ == "__main__":
    main()