n = int(input())
a = list(map(int, input().split()))
max = max(a)
min = min(a)
max_pos = a.index(max)
min_pos = n - 1 - a[::-1].index(min)
swaps = max_pos + (n - 1 - min_pos)
if max_pos > min_pos:
    swaps -= 1

print(swaps)
