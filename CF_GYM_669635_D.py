n=int(input())
for i in range(n):
    a=int(input())
    arr=list(set(map(int,input().split())))
    print(len(set(arr)))