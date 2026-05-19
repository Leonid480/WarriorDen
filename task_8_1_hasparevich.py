def fact2(n):
    res = 1
    for i in range(n, 0, -2):
        res *= i
    return res


numbers = [3, 4, 5, 6, 7]
for n in numbers:
    print(f"{n}!! = {fact2(n)}")