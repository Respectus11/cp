n=int(input())
for i in range(n):
    b=int(input())
    arr=list(map(int,input().split()))
    red=[]
    for j in range(len(arr)):
        red.append(j%2)
    arr2=[]
    for j in range(len(arr)):
        arr2.append((arr[j],j))
    arr2=sorted(arr2)
    flag=True
    for j in range(1,len(arr2)):
        if red[arr2[j][1]]==red[arr2[j-1][1]]:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")