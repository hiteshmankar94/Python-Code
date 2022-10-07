# Program which accept one number and display below pattern

def display(num):
    for i in range(num):
        for j in range(num):
            print("*", end=" ")
        print()

def main():
    ino = int(input("Enter the number:"))
    display(ino)

if __name__ == "__main__":
    main()