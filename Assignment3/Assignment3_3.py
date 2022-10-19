# Program which accept N number from user and store it into List and return minimum number from tgat list

def listmin(lst):
    min = lst[0]
    for i in range(len(lst)):
        if min > lst[i]:
            min = lst[i]
    return min

def main():
    lst = list()
    num = int(input("Enter the number of elements:"))
    print("Enter the {} elements".format(num))

    for i in range(num):
        val = int(input())
        lst.append(val)

    print("Minimum number in list is:", listmin(lst))

if __name__ == "__main__":
    main()