# a = input().strip()
# b = input().strip()
# c = input().strip()
# addd = a+b
# if sorted(addd)== sorted(c):
#     print("YES")
# else:
#     print("NO")

from collections import Counter 
a = input().strip()
b = input().strip()
c = input().strip()
add = a+b
if Counter(add)==Counter(c):
        print("YES")
else:
    print("NO")

    