n=int(input())
for i in range(n):
    n=input().strip()
    result=[]
    leng=len(n)
    for i,num in enumerate(n):
        if num !="0":
            result.append(int(num)*(10**(leng-i-1)))
    print(len(result))
    print(*result)
        