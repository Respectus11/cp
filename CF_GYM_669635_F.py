a,b=map(int,input().split())
arr =list(map(int,input().split()))
maxx=1
lenn=1
for i in range(1,a):
    if arr[i]!=arr[i-1]:
        lenn+=1
    else:
        lenn=1
    if lenn>maxx:
        maxx=lenn
print(maxx)