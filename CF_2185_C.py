n=int(input())
for i in range(n):
    a=int(input())
    arr=list(map(int,input().split()))
    arr = sorted(set(arr))
    longest = 0
    current =1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            current +=1
        else:
            if current >longest:
                longest = current
            current = 1
    if current > longest:
        longest = current
    print(longest)