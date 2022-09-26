def isPowerOfTwo(n: int) -> bool:
    # only works for integer values: 1, 2, 4, 8, 16, etc.
    return (n != 0) and (n & (n-1) == 0)


print(isPowerOfTwo(256))
print(isPowerOfTwo(0))
