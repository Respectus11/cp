n=int(input())
for i in range(n):
    n,k,x= map(int,input().split())
    if k>n:
        print("NO")
        continue
    minn=k*(k+1)//2
    maxx=k*(2*n-k+1)//2
    if minn<=x<=maxx:
        print("YES")
    else:
        print("NO")
