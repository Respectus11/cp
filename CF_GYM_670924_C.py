n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    p = 1
    while a % 2 == 0:
        a //= 2
        p *= 2
    while b % 2 == 0:
        b //= 2
        p *= 2
    print("YES" if p >= c else "NO")
