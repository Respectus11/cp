import math
a,b =map(int,input().split())
m=max(a,b)
chance=7-m
face=6
ans=math.gcd(chance,face)
print(f"{chance//ans}/{face//ans}")