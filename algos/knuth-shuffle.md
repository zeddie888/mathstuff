# Knuth Shuffle

This is an algorithm that shuffles a sequence of objects, or more formally, "generates a random permutation of a finite sequence".

Also called the Knuth Shuffle or Fisher-Yates shuffle

Two important notes:
1. This algorithm has `O(n)` runtime, `O(1)` space complexity
2. Guaranteed to produce unbiased results, assuming the random number generator is good enough
    1. Note: Python's `random` module may not be strong enough
    2. In fact, the naive shuffle is just fundamentally biased

---

## Code

Python:

```py
import random

def shuffle(arr):
  n = len(arr)
  for i in range(n-1, 0, -1):
    # pick a random integer j in range [0, i]
    j = random.randint(0, i)
    # swap arr[j] and arr[i]
    arr[i], arr[j] = arr[j], arr[i]

```

Java:

```java
import java.util.Random;

public static void shuffle(Object[] arr){
    Random r = new Random();
    for(int i = arr.length-1; i >= 1; i--){
        // pick a random integer j in range [0, i]
        int j = r.nextInt(i+1);
        // swap arr[j] and arr[i]
        Object temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

```

- Runtime `O(n)`
- Space `O(1)`, note that this implementation does the shuffle in-place

