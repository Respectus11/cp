n = int(input())
while n> 0:
    a = int(input())
    if a > 45:
        print(-1)
    else:
        ans = ""
        d =9
        while a> 0 and d > 0:
            if a>= d:
                ans=str(d) + ans 
                a -=d
            d-= 1
        print(ans)
    n -= 1
