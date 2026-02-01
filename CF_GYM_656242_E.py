t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    freq = {}
    flag = -1
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == 3: 
            flag = x
            break
    print(flag)
