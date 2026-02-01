t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    summ = sum(abs(x) for x in arr)
    operation = 0
    i = 0
    while i < n:
        if arr[i] < 0:
            operation += 1
            while i < n and arr[i] <= 0:
                i += 1
        else:
            i += 1
    
    print(summ, operation)
