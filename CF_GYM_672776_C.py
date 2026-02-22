n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    size=2*(abs(a-b))
    if size<max(a,b,c):
        print(-1)
    else:
        ans=int(c+(size/2))
        print(ans if ans<=size else ans-size)