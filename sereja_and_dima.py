n=int(input())
arr = list(map(int,input().split()))
l=0
r=n-1
serja=0
dima=0
move=0
while l<=r:
    if arr[l]>arr[r]:
        select=arr[l]
        l+=1
    else:
        select=arr[r]
        r-=1
    if move %2==0:
        serja+=select
    else:
        dima+=select
    move+=1
print(serja,dima)