# Boyer-Moore Majority Vote Algorithm

This is a quite simple yet elegant algorithm that finds the **majority element** (assuming there is one) in a sequence of $n$ elements

The majority element is the element that appears $> \left \lfloor{\frac{n}{2}}\right \rfloor$ times

---

## Main Idea:
- At all times, some element in the sequence will be your `candidate` element for majority element status
- Keep a `counter`, initialized to 0
- For every element, `x`, in the sequence:
  - If `counter == 0`, then choose new candidate. Set `counter = x`
  - If `x == candidate`, increment counter. Otherwise decrement counter
- If majority element exists for sequence, then at the end of the run, `counter` will be positive and `candidate` will be equal to the majority element
  - This is because earlier subsequences in which the number of minority elements balanced out the number of majority elements are ignored
  - Finally, number of increments to counter will be greater than the number of decreases. This happens when `candidate == majority element`

---

## Code

Java:

```java
public static int majorityElement(int[] nums) {
    Integer candidate = null;
    int count = 0;
    for(int num : nums){
        if(count == 0){
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }
    return candidate;
}

```

- Runtime `O(n)`
- Space `O(1)`