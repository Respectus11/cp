n= int(input())
arrr=list(map(int,input().split()))
maxx=0
temp=0
for i in range(1,n):
    if arrr[i]>arrr[i-1]:
        temp+=1
        maxx= max(temp,maxx)
    else:
        temp =0
print (maxx +1)