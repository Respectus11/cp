a=int(input())
arr=list(map(int,input().split()))
minn=min(arr)
maxx=max(arr)
ans=a-arr.count(minn)-arr.count(maxx)
if ans<0:
    ans=0
print(ans)
