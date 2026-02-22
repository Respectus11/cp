n=int(input())
for i in range(n):
    a,b,c=map(int,input().split())
    if a+b>9 or a+c>9 or b+c>9:
        print("YES")
    else:
        print("NO")