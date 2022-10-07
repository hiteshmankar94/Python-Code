# Program which accept number from user and return addition of digits in that number

def digit_count(num):
    dig_sum = 0
    while num != 0:
        val = num % 10
        dig_sum += val
        num = num // 10

    return dig_sum

def main():
    ino = int(input("Enter the number:"))
    print(digit_count(ino))

if __name__ == "__main__":
    main()