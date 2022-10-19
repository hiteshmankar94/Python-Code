
def ChkPrime(Num):
    Count = 0
    for i in range(1, (Num//2)+1):
        if (Num % i == 0):
            Count += 1

    if Count == 1:
        return True
