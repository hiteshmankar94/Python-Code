# Program which accept N numbers from user and store it into List and return maximum number from that List

def listmax(lst):
    max = lst[0]
    for i in range(len(lst)):
        if max < lst[i]:
            max = lst[i]
    return max

def main():
    lst = list()
    num = int(input("enter the number of elements:"))
    print("Enter the {} elements".format(num))

    for i in range(num):
        val = int(input())
        lst.append(val)

    print("Maximum number in list is:", listmax(lst))

if __name__ == "__main__":
    main()