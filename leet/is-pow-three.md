# Power of Three

From this [Leetcode Problem](https://leetcode.com/problems/power-of-three/)

```
Given an integer n, return true if it is a power of three. Otherwise, return false
```

Simple enough, if $n = 3^k$ for some integer $k$, then $\log_3x = k$
- In other words, if $n$ is a power of 3, then $\log_3x = $ some integer

---

## Code

Java:
```java
public boolean isPowerOfThree(int n) {
    double x = Math.log10(n) / Math.log10(3);
    return (x % 1) == 0;
}

```

---
## Follow-up

Something interesting - in the above code, if you  use `Math.log()` instead of `Math.log10()`, you sometimes get the wrong answer

This [SO Post](https://stackoverflow.com/questions/69323441/python-math-log-and-math-log10-giving-different-results) tells that the base-10 logarithm is "usually more accurate" than the natural log