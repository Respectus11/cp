# n = int(input())
# counter = 0 
# while n !=0:
#     if n>=100:
#         n=n-100
#         counter +=1
#     elif n>=20:
#         n= n-20
#         counter +=1
#     elif n>=10:
#         n= n-10
#         counter +=1
#     elif n>=5:
#         n= n-5
#         counter +=1
#     elif n>=1:
#         n=n-1
#         counter +=1
# print (counter)
n = int (input())
counter = 0 
for d in [ 100 , 20 ,10 ,5,1]:
    counter += n//d
    n%=d
print (counter)