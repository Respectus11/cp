a, b = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
sum = [0]
for i in p:
    sum.append(sum[-1] + i)
for j in range(b):
    x, y = map(int, input().split())
    ans = sum[a - x + y] - sum[a - x]
    print(ans)
