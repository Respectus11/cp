n=int(input())
for i in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    summ = sum(arr)
    if summ%2 ==0:
        print("YES")
    else:
        print("NO")










