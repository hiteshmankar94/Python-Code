# Program which accept number from user and return number of digits in that number

def digit_count(num):
    count = 0

    while num != 0:
        val = num % 10
        count += 1
        num = num // 10

    return count

def main():
    ino = int(input("Enter the number:"))
    print(digit_count(ino))

if __name__ == "__main__":
    main()