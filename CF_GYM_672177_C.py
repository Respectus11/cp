n = int(input())
for i in range(n):
    c = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    d = len(s)
    while d not in s:
        s.add(d)
        d += 1
    print(d)
