import numpy as np
a, b, c = map(int, input().split())
arr1 = np.array([input().split() for _ in range(a)], int)
arr2 = np.array([input().split() for _ in range(b)], int)
result = np.concatenate((arr1, arr2), axis=0)
print(result)