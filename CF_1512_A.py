from collections import Counter
n= int(input())
for i in range(n):
    a = int(input())
    b= list(map(int,input().split()))
    freq=Counter(b)
    for j ,ch in freq.items():
        if ch==1:
            print(b.index(j)+1)
            break
    