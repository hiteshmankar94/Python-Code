# Program which accept N number from user and store it into List and return addition of all elements from the List

def listadd():
    lst = list()

    num = int(input("enter the number of elements:"))
    print("Enter the {} elements".format(num))
    for i in range(num):
        val = int(input())
        lst.append(val)

    add = 0
    for no in range(len(lst)):
        add = add + lst[no]
    print(add)

def main():
    listadd()

if __name__ == "__main__":
    main()