from helper import *

n = 12

sum = 0
for i in range(0, n+1):
  print(i)
  sum += C(n, i)
print("sum", sum)

print("another sum", 2**n)

