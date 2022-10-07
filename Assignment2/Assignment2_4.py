# Program which accept one number from user and return addition of its factors

def factor(num):
    fact_add = 0
    for i in range(1, (num//2)+1):
        if (num % i == 0):
            fact_add += i
    return fact_add

def main():
    ino = int(input("Enter the number to find factor:"))
    print(factor(ino))

if __name__ == "__main__":
    main()
