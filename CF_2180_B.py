n= int(input())
for i in range(n):
    a= int(input())
    arr= input().split()
    s=""
    for j in arr:
        front = j + s
        back = s + j
        if front < back:
            s = front
        else:
            s = back
    print(s)

        