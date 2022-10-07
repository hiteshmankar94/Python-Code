def display(num):
    for i in range(num):
        print("*", end="    ")

def main():
    ino = int(input("Enter the number:"))
    display(ino)

if __name__ == "__main__":
    main()