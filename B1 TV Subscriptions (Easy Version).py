t = int(input())
for i in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    ans = d
    for i in range(n - d + 1):
        wind = a[i:i+d]
        dis = len(set(wind))
        ans = min(ans, dis)

    print(ans)
