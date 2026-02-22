n = int(input())
for i in range(t):
    a= int(input())
    ans = []
    for k in range(1, 19):  # check up to 18 zeros
        div= 1 + 10**k
        if n % divisor == 0:
            x = n // divisor
            and.append(x)
    if not results:
        print(0)
    else:
        print(len(results))
        print(*sorted(results))
