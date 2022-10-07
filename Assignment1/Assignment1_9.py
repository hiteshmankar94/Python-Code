#Write a program which display first 10 even numbers on screen.

def even_num():
    i=1
    for i in range(1, 21):
        if(i % 2 == 0):
            print(i, end="   ")

def main():
    even_num()

if __name__ == "__main__":
    main()
