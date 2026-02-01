n= int(input())
arr=list(map(int,input().split()))
maxx=max(arr)
counter= 0
for i in arr:
    counter+=(maxx-i)
print(counter)