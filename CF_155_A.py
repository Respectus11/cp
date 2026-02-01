n= int(input())
arr = list(map(int,input().split()))
minn= arr[0]
maxx = arr[0]
           
count = 0
for i in arr[1:]:
    if i>maxx:
        count += 1
        maxx = i
    elif i<minn:
        count +=1
        minn = i
print (count)


