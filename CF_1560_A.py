n=int(input())
for i in range(n):
    a = int(input())
    arr = []  
    j = 1
    while len(arr) < a:
        if j % 3 != 0 and j % 10 != 3:
            arr.append(j)
        j += 1
    print(arr[a - 1])
