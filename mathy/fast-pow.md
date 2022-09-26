# Fast Powers

A couple ways to quickly calculate $x^n$, where $n\in \mathbb{Z}$

## Naive

Python:

```py
def naivePow(x, n) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    res = 1
    for i in range(n):
        res *= x
    return res

```
---

## Recursion

Notice that:

$$
x^n=
\begin{cases}
x(x^2)^{\frac{n-1}{2}} & \quad \text{if $n$ is odd} \\
(x^2)^\frac{n}{2} & \quad \text{if $n$ is even}
\end{cases}
$$


Python:

```py
def fastPow1(x, n):
    if n < 0:
        return fastPow1(1/x, -n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return fastPow1(x*x, n/2)
    if n % 2 == 1:
        return x * fastPow1(x*x, (n-1)/2)


```

Java:

```java
public double fastPow(double x, long n){
    if(n < 0) return fastPow(1 / x, -n);
    if(n == 0) return 1;
    if(n % 2 == 0){
        return fastPow(x*x, n/2);
    }else{
        return x * fastPow(x*x, (n-1)/2);
    }
}

```

- Runtime `O(log n)` for $x^n$
- Space `O(log n)`

---

## TODO

The same algorithm can be implemented both iteratively and using tail-recursion, so cutting space down to `O(1)`

