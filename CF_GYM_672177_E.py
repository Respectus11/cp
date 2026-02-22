k = int(input())
for i in range(k):
    n = int(input())
    p = list(map(int, input().split()))
    found = False
    for j in range(1, n - 1):  
        if p[j] > p[j - 1] and p[j] > p[j + 1]:
            print("YES")
            print(j, j + 1, j + 2)
            found = True
            break
    if not found:
        print("NO")
