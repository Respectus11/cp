k = int(input()) 
for i in range(k):
    n, a = map(int, input().split())  
    arr = list(map(int, input().split()))  
    best = arr[0]
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= a:
            left = mid + 1
        else:
            best = arr[mid]
            right = mid - 1

    print(best)
