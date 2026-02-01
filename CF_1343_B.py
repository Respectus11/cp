t = int(input())
for i in range(t):
    n = int(input())
    if (n // 2) % 2:
        print("NO")
    else:
        print("YES")
        for i in range(1, n//2+1):
            evens = [2*i]
        for i in range(1, n//2):
            odds = [2*i-1]
        odds.append(sum(evens) - sum(odds))
        print(*evens, *odds)
