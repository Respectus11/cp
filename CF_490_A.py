from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
c = Counter(arr)
w = min(c[1], c[2], c[3])
print(w)
prog, math, pe = [], [], []
for i, j in enumerate(arr, start=1):
    if j == 1:
        prog.append(idx)
    elif j == 2:
        math.append(idx)
    else:
        pe.append(idx)
for i in range(w):
    print(prog[i], math[i], pe[i])
