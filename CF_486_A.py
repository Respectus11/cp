# n= int(input())
# counter =0
# for i in range(1,n+1):
#    counter += ((-1)**i)*i
   
# print (counter)


n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-(n + 1) // 2)