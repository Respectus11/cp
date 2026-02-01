n=int(input())
for i in range(n):
    a,b = map(int,input().split())
    d =list(map(int, input().split()))
    if b in d:
        print("YES")
    else:
        print("NO")
    
