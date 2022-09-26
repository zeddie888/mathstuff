def naivePow(x, n) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    for i in range(n):
        res *= x
    return res


def fastPow1(x, n):
    if n < 0:
        return fastPow1(1/x, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return fastPow1(x*x, n/2)
    if n % 2 == 1:
        return x * fastPow1(x*x, (n-1)/2)


print(naivePow(2, 3))
print(naivePow(3, -4))
