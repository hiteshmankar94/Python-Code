#Write a program which display 10 to 1 on screen.

def num_display():
    for i in range(10, 0, -1):
        print(i, end="  ")

def main():
    num_display()

if __name__ == "__main__":
    main()
