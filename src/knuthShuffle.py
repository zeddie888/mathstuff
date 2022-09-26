import random

def shuffle(arr):
  n = len(arr)
  for i in range(n-1, 0, -1):
    # pick a random integer j in range [0, i]
    j = random.randint(0, i)
    # swap arr[j] and arr[i]
    arr[i], arr[j] = arr[j], arr[i]

arr = list(range(10))
print(arr)
for i in range(10):
  shuffle(arr)
  print(arr)
