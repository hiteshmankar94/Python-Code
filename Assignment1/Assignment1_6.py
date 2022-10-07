def number(val):
    if val > 0:
        return "Positive Number"
    elif val < 0:
        return "Negative Number"
    else:
        return "Zero"

def main():
    ino = int(input("Enter the number:"))
    print(number(ino))

if __name__ == "__main__":
    main()