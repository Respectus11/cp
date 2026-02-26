n = int(input())
for i in range(n):
    b=int(input())
    a = list(map(int, input().split()))
    sortedd = sorted([abs(x) for x in a])
    mediann = (b + 1) // 2-1  
    if abs(a[0]) == sortedd[mediann]:
        print("YES")
    else:
        print("NO")
#wrong i will see this again