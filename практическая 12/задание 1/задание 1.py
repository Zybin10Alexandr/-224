def F():
    n = int(input())
    if n == 0:
        return int()
    return max([n, F()])
print(F())