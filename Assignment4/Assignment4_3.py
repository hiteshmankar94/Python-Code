# Python application program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers.
# List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and
# less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all that numbers.

from functools import reduce
def main():

    Data_lst = []

    Num = int(input("Enter the number of elements:"))
    print("Enter the {} number of elements:".format(Num))

    for a in range(Num):
        Value = int(input())
        Data_lst.append(Value)

    Data_filter = list(filter(lambda A: A>=70 and A<=90, Data_lst))

    print("List after filter", Data_filter)

    Data_Map = list(map(lambda A: A+10, Data_filter))
    print("List after map", Data_Map)

    Data_reduced = reduce(lambda A ,B: A * B, Data_Map)
    print("Output of reduce", Data_reduced)

if __name__ == "__main__":
    main()