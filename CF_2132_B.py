t = int(input())
for i in range(t):
    n = int(input())
    results = []
    for k in range(1, 19):
        divisor = 1 + 10**k
        if n % divisor == 0:
            results.append(n // divisor)
    if results:
        print(len(results), *sorted(results))
    else:
        print(0)
