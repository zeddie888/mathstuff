# Is Power of Two

Here's an elegant way to check if a number `n` is a power of 2

The key thing is to look at the binary notation for decimal number `n`

If `n` is a power of 2, then its binary number is a 1 followed by all 0s

- For example, let `n = 8`. Its binary number is: `1000`

Now take a look at `n-1` if `n` is a power of 2. Its binary number contains all 1s. The number of 1s == the number of trailing 0s in `n`.

- For example, take `n = 7`. Its binary number is: `0111`

Observe that if we perform bitwise `AND (&)` between `n` and `n-1`:

```
(n & (n-1) == 0) if and only if n is a power of 2
```

So, our initial code can look like:

Python:
```py
# BUG
def isPowerOfTwo(n: int) -> bool:
    # only works for integer values: 1, 2, 4, 8, 16, etc.
    return (n & (n-1)) == 0
```

There is a small bug. `0` is not a power of 2, but `0 & anything == 0`, so our function returns `True`

To deal with this, simply add an extra case for 0:

Python:
```py
def isPowerOfTwo(n: int) -> bool:
    # only works for integer values: 1, 2, 4, 8, 16, etc.
    return (n != 0) and (n & (n-1) == 0)
```

