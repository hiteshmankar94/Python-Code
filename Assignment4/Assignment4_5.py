# Program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted from user.
# Filter should filter out all prime numbers. Map function will multiply each number by 2. Reduce will return Maximum number from that numbers.
from functools import reduce

def ChkPrime(No):
    Count = 0
    for i in range(1, (No//2)+1):
        if No % i ==0:
            Count += 1
    if Count == 1:
        return True
    else:
        return False

def main():

    Data_lst = []

    Num = int(input("Enter the number of elements:"))
    print("Enter the {} number of elements:".format(Num))

    for a in range(Num):
        Value = int(input())
        Data_lst.append(Value)

    Data_filter = list(filter(ChkPrime, Data_lst))

    print("List after filter", Data_filter)

    Data_Map = list(map(lambda A: A * 2, Data_filter))
    print("List after map", Data_Map)

    Data_reduced = reduce(lambda A ,B: A if (A > B) else B, Data_Map)
    print("Output of reduce", Data_reduced)

if __name__ == "__main__":
    main()