n = int(input())
for i in range(n):
    a, k = map(int, input().split())
    arr = input().strip()
    awake = -1
    count = 0
    for i in range(a):
        if arr[i] == '1':
            awake = i + k
        elif arr[i] == '0' and i > awake:
            count += 1
    print(count)
