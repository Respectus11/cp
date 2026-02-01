k = int(input())
for i in range(k):
    a, b, n = map(int, input().split())
    m= a // b 
    if n <= m:
        print(1)
    else:
        if a%b == 0:
            print(1)
        else:
            print(2)
