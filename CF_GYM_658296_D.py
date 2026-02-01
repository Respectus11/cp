n = int(input())
for i in range(n):
    a = input().strip()
    b = input().strip()
    l = 0 #pointer 
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            l += 1
        else:
            break
    if l == 0:
        print(len(a) +len(b))
    else:
        print(len(a) + len(b) - l + 1)
