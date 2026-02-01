a,b = map(int,input().split())
arr= list(map(int,input().split()))
counter =0
for i in arr:
    if i + b<=5:
        counter+=1
print (counter//3)