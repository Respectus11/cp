t = int(input())
for i in range(t):
    n, x, y = map(int, input().split())
    s = input().strip()
    e = s.count('8')
    f = s.count('4')
    a, b = abs(x), abs(y)
    d = min(e, min(a, b))
    L = a + b - 2 * d
    R = f + (e - d)
    if L <= R:
        print("YES")
    else:
        print("NO")
