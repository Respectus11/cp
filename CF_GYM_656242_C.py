n = int(input())
taken = list(map(int, input().split()))
a=0
b=0
index = 0 
while taken:
    if taken[0] >= taken[-1]:
        selected = taken.pop(0)   
    else:
       selected = taken.pop()   
    if index % 2 == 0:
        a += selected
    else:
        b += selected
    index += 1

print(a, b)
