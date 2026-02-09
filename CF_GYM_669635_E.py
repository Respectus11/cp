from collections import Counter
n =int(input())
names=[]
counter=Counter()
for i in range(n):
    a=input()
    if counter[a]==0:
        print("OK")
    else:
        print(f"{a}{counter[a]}")
    counter[a]+=1
    names.append(a)