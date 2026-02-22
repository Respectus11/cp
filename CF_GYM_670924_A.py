n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    summ=(a*60)+b
    print(1440-summ)