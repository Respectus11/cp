n=int(input())
for i in range(n):
    a=input()
    store=[]
    for i in range(len(a)):
        if a[i]!="0":
            store.append(a[i]+'0'*(len(a)-i-1))
    print(len(store))
    print(*store)
