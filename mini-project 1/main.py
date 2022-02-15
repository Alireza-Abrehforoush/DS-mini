import numpy as np
d = 4000
n = 10000
arr = []
brr = []
for i in range(n):
    x = np.random.normal(size = d)
    y = np.linalg.norm(x)
    r = np.random.random()
    arr.append(r ** (1 / d) * (x / y))
for i in range(n):
    brr.append(np.linalg.norm(arr[i]))
print(sum(brr)/len(arr))