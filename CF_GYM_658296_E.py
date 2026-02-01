n =int(input())
arr =list(map(int, input().split()))
asend =sorted(arr)
b =int(input())
for i in range(b):
    c,d,e =map(int, input().split())
    if c == 1:
        print(sum(arr[d-1:e]))
    else:
        print(sum(asend[d-1:e]))
