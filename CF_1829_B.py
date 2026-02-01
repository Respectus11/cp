n= int(input())
for j in range(n):
    a= int(input())
    arr=list(map(int,input().split()))
    maxx=0
    temp=0
    for i in arr:
        if i==0:
            temp+=1
            maxx=(max(maxx,temp)) 
        else:
            temp= 0
    print(maxx)
    