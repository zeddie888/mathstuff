# Euclid's Algorithm for GCD (basic)

> TODO: proof

This is a super useful algorithm that computes the GCD (greatest common divisor) of two integers (assume nonnegative)

Two essential facts:
1. `gcd(a, 0) = a` for any positive integer `a`
- Since $a | a$ and $a | 0$
- Note that `gcd(0, 0)` is not defined

2. `gcd(a, b) = gcd(b, a mod b)` for all positive ints `a, b`


## Code

Python:

```python
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a % b)

```


Java:

```java
public static int gcd(int a, int b){
  if(b == 0) return a;
  return gcd(b, a % b);
}

```
