t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = float('inf')
    for i in range(n - 1):
        ans = min(ans, max(a[i], a[i+1]))
    print(ans - 1)
