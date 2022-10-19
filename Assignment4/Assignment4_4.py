# Program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even. Map function will calculate its square. Reduce will return addition of all that numbers

from functools import *

def main():
    Data_lst = []
    Num = int(input("Enter the number of elements:"))

    print("Enter the {} number of elements:".format(Num))

    for a in range(Num):
        Value = int(input())
        Data_lst.append(Value)

    Data_filter = list(filter(lambda A: A % 2 == 0, Data_lst))
    print("List after filter:", Data_filter)

    Data_map = list(map(lambda A : A ** 2, Data_filter))
    print("List after map", Data_map)

    Output = reduce(lambda A,B : A + B, Data_map)
    print("Output of reduce", Output)


if __name__ == "__main__":
    main()