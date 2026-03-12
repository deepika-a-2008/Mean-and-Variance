import numpy as np
L = [int(i) for i in input("Enter arrival data: ").split()]
N = len(L)
M = max(L)
X = []
f = []
for i in range(M + 1):
    c = 0
    for j in range(N):
        if L[j] == i:
            c += 1
    f.append(c)
    X.append(i)
sf = np.sum(f)
p = [f[i] / sf for i in range(M + 1)]
mean = np.inner(X, p)
EX2 = np.inner(np.square(X), p)
var = EX2 - mean**2
SD = np.sqrt(var)
print("\nX\tp(x)")
for i in range(M + 1):
    if f[i] > 0:   
        print(f"{X[i]}\t{p[i]:.3f}")
print(f"\nThe Mean arrival rate is {mean:.3f}")
print(f"The Variance of arrival from feeder is {var:.3f}")
print(f"The Standard deviation of arrival from feeder is {SD:.3f}")
