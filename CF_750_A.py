a, b = map (int,input().split())
remain = 240 -b
summ= 0
counter = 0
for i in range(1,a+1):
    if summ+5*i<=remain:
        summ+=i*5
        counter+= 1
print(counter)

    