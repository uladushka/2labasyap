import random

M = 3
N = 3
A = [[0]*N for i in range(M)]
for i in range(M):
    for j in range(N):
        A[i][j] = (random.randint(-10, 10))

print(A)
count = 0
for i in range(M):
    for j in range(N):
        if A[i][j] > 0:
            count += 1
            break

if count != 0:
    for i in range(M):
        for j in range(N):
            A[i][j] = -A[i][j]

print(A)