
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