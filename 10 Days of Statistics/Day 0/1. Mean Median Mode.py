import sys
import numpy as np

n = int(sys.stdin.readline())
a = np.array(sorted(list(map(int, sys.stdin.readline().split()))))
print(np.mean(a))
print(np.median(a))
(_, idx, counts) = np.unique(a, return_index=True, return_counts=True)
index = idx[np.argmax(counts)]
mode = a[index]
print(mode)