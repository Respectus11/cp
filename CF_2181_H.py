w, h, d = map(int, input().split())
n = int(input())

a = b = c = 1
x = n
p = 2

while p * p <= x:
    while x % p == 0:
        if w % (a * p) == 0:
            a *= p
        elif h % (b * p) == 0:
            b *= p
        elif d % (c * p) == 0:
            c *= p
        else:
            print(-1)
            exit()
        x //= p
    p += 1

if x > 1:
    if w % (a * x) == 0:
        a *= x
    elif h % (b * x) == 0:
        b *= x
    elif d % (c * x) == 0:
        c *= x
    else:
        print(-1)
        exit()

print(a - 1, b - 1, c - 1)
