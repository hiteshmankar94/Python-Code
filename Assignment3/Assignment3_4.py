# Program which accept N number from user and store it into List.
# Accept one another number from user and return frequency of that number from list

def numberfreq(lst, No):
    numbercount = 0
    for i in range(len(lst)):
        if No == lst[i]:
            numbercount += 1
    return numbercount

def main():
    lst = list()
    num = int(input("enter the number of elements:"))
    print("Enter the {} elements".format(num))

    for i in range(num):
        val = int(input())
        lst.append(val)

    No = int(input("Enter the number to find its frequency:"))

    print("Frequency of number in list is:", numberfreq(lst, No))

if __name__ == "__main__":
    main()