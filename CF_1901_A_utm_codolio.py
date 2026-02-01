n=int(input())
for i in range(n):
    L, N = map(int, input().split())
    points = list(map(int, input().split()))

    points.append(0)
    points.append(L)

    points.sort()

    ans = 0
    for i in range(1, len(points)):
        if points[i] - points[i-1] > ans:
            ans = points[i] - points[i-1]

    print(ans)
