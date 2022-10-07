# Program which accept one number for user and check whether number is prime or not

def check_prime(num):
    count = 0
    for i in range(1, (num//2)+1):
        if (num % i == 0):
            count += 1

    if count > 1:
        print("It is not Prime Number")
    else:
        print("It is Prime Number")

def main():
    ino = int(input("Enter the number to check Prime Number or not:"))
    check_prime(ino)

if __name__ == "__main__":
    main()
