# Single Number

Fom this [Leetcode Problem](https://leetcode.com/problems/single-number/):

```
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
```

## Bit Manipulation

This provides us with a `O(n)` runtime, `O(1)` space solution

Recall the bitwise XOR operation
- For each pair of corresponding bits, we perform the logical exclusive OR operation. This operation returns true if only one of the arguments is true
- `1 ^ 1 == 0`
- `0 ^ 0 == 0`
- `0 ^ 1 == 1`
- `1 ^ 0 == 1`


Two important observations:

1. $a \oplus a = 0$
2. $a \oplus 0 = a$

So if we XOR together all elements of `nums`, the elements that appear twice will XOR to 0, leaving us the unique number at the end.

## Code

Java:
```java
public int singleNumber(int[] nums) {
    int res = 0;
    for(int num : nums){
        res = (res ^ num);
    }
    return res;
}

```