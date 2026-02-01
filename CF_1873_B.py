n = int(input())
for i in range(n):
    b= int(input())
    a = list(map(int, input().split()))
    max_product = 0
    for i in range(b):
        b = a[:]              # copy array
        b[i] += 1             # add 1 to one digit
        product = 1
        for x in b:
            product *= x
        max_product = max(max_product, product)
    
    print(max_product)
