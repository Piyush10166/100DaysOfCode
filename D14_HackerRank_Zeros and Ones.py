import numpy as np

shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int), np.ones(shape, dtype=int), sep='\n')