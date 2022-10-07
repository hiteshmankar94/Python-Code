# Program which accept one number and display pattern

def display_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print("*", end=" ")
        print()

def main():
    ino = int(input("Enter the number:"))
    display_pattern(ino)

if __name__ == "__main__":
    main()