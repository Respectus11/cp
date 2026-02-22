arr=list(map(int,input().split()))
maxx=max(arr)
arr2=[]
for i in arr:
    if maxx==i:
        continue
    else:
        arr2.append(maxx-i)
print(*arr2)