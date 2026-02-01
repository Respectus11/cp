n = int(input())
for i in range(n):
    a =int(input())
    b =list(map(int, input().split()))
    l =b[0]
    r =b[0]
    flag =True
    for i in b[1:]:
        if i == l - 1:
            l -= 1
        elif i == r + 1:
            r += 1
        else:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
    

