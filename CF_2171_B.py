k = int(input())
for i in range(k):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != -1 and a[-1] != -1:
        ans = abs(a[-1] - a[0])
    elif a[0] != -1:
        a[-1] = a[0]
        ans = 0
    elif a[-1] != -1:
        a[0] = a[-1]
        ans = 0
    else:
        a[0] = a[-1] = 0
        ans = 0
    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    print(ans)
    print(*a)
