#  Write a program which contains one function named as ChkNum() which accept one
#  parameter as number. If number is even then it should display “Even number” otherwise  display “Odd number” on console.

def ChkNum(num):
    if num%2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def main():
    val = int(input("Enter the number:"))
    print(ChkNum(val))

if __name__ == "__main__":
    main()
