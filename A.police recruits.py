n=int(input())
arr=list(map(int,input().split()))
stored =0
chk =0
for i in arr:
    if i==-1:
        if stored>0:
            stored -=1
        else:
            chk +=1
    else:
        stored+=i
print(chk)


