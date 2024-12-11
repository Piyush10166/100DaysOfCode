import numpy as np

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
np_arr = np.array(arr)

print(np_arr.T)
print(np_arr.flatten())