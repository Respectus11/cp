a,b=map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in range(a):
    if arr[i] <= b:
        count+=1
    else:
        count+=2
print(count)