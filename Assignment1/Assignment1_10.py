#Write a program which accept name from user and display length of its name.

def name_length(name):
    count = 0
    for i in name:
        count+= 1

    return count

def main():
    istr = input("Enter the name:")
    print(name_length(istr))

    # directly with function
    # print(len(istr))

if __name__ == "__main__":
    main()
