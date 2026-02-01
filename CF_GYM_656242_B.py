x = int(input())
for i in range(x):
    a,b,c = map(int ,input().split())
    if a+c>=10 or a+b>=10 or b+c>=10:
        print("YES")
    else:
        print("NO")